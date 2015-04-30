import time
import os
import shutil
from shapely.geometry import shape
import fiona
from fiona import collection
from rtree import index
from geobricks_common.core.filesystem import get_filename
from multiprocessing import Process, Queue, Pool



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
            if s['properties'].get('DISP_AREA') == 'NO' and s['properties'].get('STATUS') == 'Member State':
                id = int(s['id'])
                code = int(s['properties'].get(property))
                geom = shape(s['geometry'])
                idx.insert(id, geom.bounds)
                features[id] = (s, geom, code)
        return idx, features


def test(input_shp, outputfolder, idx, features):

    print "Reading input shp: ", input_shp
    with fiona.open(input_shp) as shp:
        sink_schema = shp.schema.copy()
        filespath = {}
        #print features
        # for f in features:
        #     f, geom, code = features[f]
        #     print code


        cached_outputfiles = {}
        # create folder structure
        print "Preparing shapefiles"
        for f in features:
            f, geom, code = features[f]
            output_folder_code = os.path.join(outputfolder, str(code))
            # TODO: remove it from here
            if os.path.isdir(output_folder_code):
                shutil.rmtree(output_folder_code)
            os.makedirs(output_folder_code)

            # TODO: write directly? How to track unsed shp?
            output_filepath = os.path.join(output_folder_code, get_filename(input_shp) + ".shp")
            cached_outputfiles[code] = fiona.open(output_filepath, 'w', crs=shp.crs, driver=shp.driver, schema=sink_schema)

        print 'End Sink files preparation'

        q = Queue()
        pool = Pool(2) #use all available cores, otherwise specify the number you want as an argument
        processes = []
        print 'Filling shapefiles'
        for feat in shp:
            geom = shape(feat['geometry'])
            for id in list(idx.intersection(geom.bounds)):
                if id != int(feat['id']):
                    # check geometry intersection
                    feat1, geom1, code = features[id]

                    #print feat['id'], str(id), str(code)

                    # additional check if the geom is in the geometry (and not only in the bounding box)
                    if geom1.intersection(geom):
                        print feat['id'], str(id), str(code)

                        # write sink
                        cached_outputfiles[code].write(feat)

        for f in cached_outputfiles:
            cached_outputfiles[f].close()




input_gaul = '/home/vortex/Desktop/LAYERS/GAUL/GAUL_2014/3857_WebMercatorAuxiliarySphere/GAUL0/G2014_2013_0_mid.shp'
#input_gaul = '/home/vortex/Desktop/LAYERS/GAUL/simone/ita.shp'
input_shp = '/home/vortex/Desktop/LAYERS/ghg/process_data/3857/CH4_Emissions_Burning_ClosedShrublands/CH4_GFED4BA_Emissions_Burning_ClosedShrublands_1997_3857.shp'
filapath = '/home/vortex/Desktop/LAYERS/GAUL/simone/ita.shp'
output_folder = '/home/vortex/Desktop/LAYERS/ghg/process_data/3857/CH4_Emissions_Burning_ClosedShrublands/gaul0/'

print "Preparing index"
start = time.time()
#features = {}
#idx = index.Rtree('bulk', build_index(input_gaul, features, 'ADM0_CODE'))
idx, features = build_index_slow(input_gaul, 'ADM0_CODE')
end = time.time()
print "End index preparation in: " + str(end - start) + " sec"


start = time.time()
test(input_shp, output_folder, idx, features)
end = time.time()
print "End Creating shapefiles in: " + str(end - start) + " sec"