import os
import glob
import shutil
from geobricks_gis_vector.core.vector import crop_shp_by_shp
from geobricks_common.core.filesystem import get_filename
import time


def extract_layer_by_all_countries(input_folder, gaul_folder, base_output_folder):
    start = time.time()
    shp_files = glob.glob(os.path.join(input_folder, "*.shp"))
    print "Shp input files: ", str(len(shp_files))
    gaul_shp_files = glob.glob(os.path.join(gaul_folder, "*.shp"))
    print "Shp gaul files: ", str(len(gaul_shp_files))
    print "Shp output files: ", str(len(shp_files) * len(gaul_shp_files))
    counter = 0
    for shp_file in shp_files:
        for gaul_shp_file in gaul_shp_files:
            print "Clipping: " + get_filename(shp_file), get_filename(gaul_shp_file)
            output_folder = os.path.join(base_output_folder, get_filename(gaul_shp_file))
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            counter = counter +1
            extract_layer(shp_file, gaul_shp_file, output_folder)
    print counter
    end = time.time()
    print "All processing done in: ", str(end - start), " sec"


def extract_layer(input_path, crop_shp_path, output_folder):
    start = time.time()

    #crop_shp_path = '/home/vortex/Desktop/LAYERS/GAUL/GAUL_2014/3857_WebMercatorAuxiliarySphere/g2014_2013_0/countries/1.shp'
    #input_path = '/home/vortex/Desktop/LAYERS/ghg/process_data/3857/CH4_Emissions_Burning_ClosedShrublands/CH4_GFED4BA_Emissions_Burning_ClosedShrublands_1997_3857.shp'
    output_name = get_filename(input_path).lower()

    try:
        # Clip file
        clipped_output_path = crop_shp_by_shp(input_path, crop_shp_path, output_name)
        clipped_folder, clipped_filename_ext, clipped_filename = get_filename(clipped_output_path, True)

        output_files = glob.glob(os.path.join(clipped_folder, "*"))

        # move files to output_folder
        for f in output_files:
            # copy with overwrite
            shutil.copy(f, output_folder)

        # remove clipped files
        shutil.rmtree(clipped_folder)
        end = time.time()
        print "Done in: " + str(end - start), " sec"
    except Exception,e:
        print "Error: ", str(e)




# input_folder = '/home/vortex/Desktop/LAYERS/ghg/process_data/3857/CH4_Emissions_Burning_ClosedShrublands/'
# gaul_folder = '/home/vortex/Desktop/LAYERS/GAUL/GAUL_2014/3857_WebMercatorAuxiliarySphere/g2014_2013_0/countries/'
# output_folder = '/home/vortex/Desktop/LAYERS/ghg/process_data/3857/CH4_Emissions_Burning_ClosedShrublands/gaul0/'
#
# shutil.rmtree(output_folder)
# extract_layer_by_all_countries(input_folder, gaul_folder, output_folder)


extract_layer('/home/vortex/Desktop/LAYERS/ghg/process_data/3857/CH4_Emissions_Burning_ClosedShrublands/CH4_GFED4BA_Emissions_Burning_ClosedShrublands_1998_3857.shp', '/home/vortex/Desktop/LAYERS/GAUL/simone/brazil/brazil.shp', '/home/vortex/Desktop/LAYERS/GAUL/simone/brazil/countries/')