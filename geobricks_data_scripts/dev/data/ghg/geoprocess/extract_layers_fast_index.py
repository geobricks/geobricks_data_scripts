import time
import sys
import os
import shutil
import glob
from shapely.geometry import shape, mapping
import fiona
from fiona import collection
from rtree import index
from geobricks_common.core.filesystem import get_filename
from progressbar import Counter, ProgressBar, Timer


def build_index(filepath, features, property=None):
    with collection(filepath, "r") as shapes:
        for s in shapes:
            geom = shape(s['geometry'])
            code = int(s['properties'].get(property))
            id = int(s['id'])
            features[id] = (s, geom, code)
            yield (id, geom.bounds, s)

def build_index_slow(filepath, property):
    with fiona.open(filepath, 'r') as layer:
        features = {}
        idx = index.Index()

        for s in layer:
            if s['properties'].get('DISP_AREA') == None:
                id = int(s['id'])
                code = int(s['properties'].get(property))
                geom = shape(s['geometry'])
                idx.insert(id, geom.bounds)
                features[id] = (s, geom, code)
        return idx, features


def extraxt_data(input_shp, outputfolder, idx, features):

    print "Reading input shp: ", input_shp
    with fiona.open(input_shp) as shp:
        sink_schema = shp.schema.copy()

        # TODO: check which countries are written (and delete the unused folders)

        # create caching folder structure
        cached_outputfiles = {}
        cached_written_files = {}
        print "Preparing shapefiles"
        for f in features:
            f, geom, code = features[f]
            output_folder_code = os.path.join(outputfolder, str(code))
            if not os.path.isdir(output_folder_code):
                #shutil.rmtree(output_folder_code)
                os.makedirs(output_folder_code)

            # TODO: write directly? How to track unsed shp?
            output_filepath = os.path.join(output_folder_code, get_filename(input_shp) + ".shp")
            cached_outputfiles[code] = fiona.open(output_filepath, 'w', crs=shp.crs, driver=shp.driver, schema=sink_schema)
            cached_written_files[code] = False

        # print 'End Sink files preparation'
        # print 'Processing shapefiles'

        # creating progress bar
        widgets = ['Processed: ', Counter(), '/', str(len(shp)), ' in ', Timer()]
        pbar = ProgressBar(widgets=widgets, maxval=len(shp))
        pbar.start()
        count_tot = 0
        for feat in shp:
            count_tot += 1
            pbar.update(count_tot)

            geom = shape(feat['geometry'])
            for id in list(idx.intersection(geom.bounds)):
                if id != int(feat['id']):
                    # check geometry intersection
                    feat1, geom_feature, code = features[id]

                    # additional check if the geom is in the geometry (and not only in the bounding box)
                    # and calculate the intersection
                    intersection = geom_feature.intersection(geom)
                    if intersection:
                        # change the feature with the new feature geometry
                        feat['geometry'] = mapping(intersection)
                        # write sink
                        cached_outputfiles[code].write(feat)
                        cached_written_files[code] = True

        # destroy progress bar
        pbar.finish()

        # Close cached outputfiles
        for f in cached_outputfiles:
            cached_outputfiles[f].close()

        # Removed not filled files
        for f in cached_written_files:
            if cached_written_files[f] is False:
                folder, filename_ext, filename = get_filename(cached_outputfiles[f].path, True)
                files_to_remove = glob.glob(os.path.join(folder, filename + ".*"))
                for file_to_remove in files_to_remove:
                    os.remove(file_to_remove)

                # remove folder if empty
                if len(os.listdir(folder)) == 0:
                    #print folder
                    shutil.rmtree(folder)



