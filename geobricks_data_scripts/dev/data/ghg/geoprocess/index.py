import time
import glob
import os
import shutil
from geobricks_data_scripts.dev.data.ghg.geoprocess.extract_layers_fast_index import build_index_slow, extraxt_data


def get_index(path, property):
    print "Preparing index"
    start = time.time()
    idx, features = build_index_slow(path, property)
    end = time.time()
    print "End index preparation in: " + str(end - start) + " sec"
    return idx, features



def process_folder(idx, features, input_folder, output_folder):
    files = glob.glob(os.path.join(input_folder, "*.shp"))

    # make the output folder
    if os.path.isdir(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder)

    for input_shp in files:
        print "Processing: ", input_shp
        start = time.time()
        extraxt_data(input_shp, output_folder, idx, features)
        end = time.time()
        print "End processing in: " + str(end - start) + " sec of ", input_shp
        print "------------------"



if __name__ == "__main__":

    # TODO: Per paolo
    # folder con problemi
    # /home/vortex/Desktop/LAYERS/ghg/process_data/3857/Peatlands_EF/


    input_gaul = '/home/vortex/Desktop/LAYERS/GAUL/GAUL0_FAOSTAT_3857_PROSPERI/GAUL_FAOSTAT_3857_PROSPERI.shp'
    idx, features = get_index(input_gaul, 'ADM0_CODE')

    # base input folder
    base_input_folder = '/home/vortex/Desktop/LAYERS/ghg/process_data/3857/'
    base_output_folder = '/home/vortex/Desktop/LAYERS/ghg/process_data/test_output/'

    folders = glob.glob(base_input_folder + "*")
    for folder in folders:
        if os.path.isdir(folder):
            dirname = os.path.basename(folder)
            input_folder = folder
            output_folder = os.path.join(base_output_folder, dirname)
            process_folder(idx, features, input_folder, output_folder)


    # # CultivationOrganicSoils
    # path = 'CultivationOrganicSoils'
    # input_folder = os.path.join(base_input_folder, path)
    # output_folder = os.path.join(base_output_folder, path)
    # process_folder(idx, features, input_folder, output_folder)
    #
    # # DM_Burning_ClosedShrublands
    # path = 'DM_Burning_ClosedShrublands'
    # input_folder = os.path.join(base_input_folder, path)
    # output_folder = os.path.join(base_output_folder, path)
    # process_folder(idx, features, input_folder, output_folder)
    #
    # # DM_Burning_Grasslands
    # path = 'DM_Burning_Grasslands'
    # input_folder = os.path.join(base_input_folder, path)
    # output_folder = os.path.join(base_output_folder, path)
    # process_folder(idx, features, input_folder, output_folder)
    #
    # # fuel biomass
    # path = 'FuelBiomass'
    # input_folder = os.path.join(base_input_folder, path)
    # output_folder = os.path.join(base_output_folder, path)
    # process_folder(idx, features, input_folder, output_folder)
    #
    # # Savanna_and_Grassland_EF
    # path = 'Savanna_and_Grassland_EF'
    # input_folder = os.path.join(base_input_folder, path)
    # output_folder = os.path.join(base_output_folder, path)
    # process_folder(idx, features, input_folder, output_folder)
    #
    # # Tropical_Forests_EF
    # path = 'Tropical_Forests_EF'
    # input_folder = os.path.join(base_input_folder, path)
    # output_folder = os.path.join(base_output_folder, path)
    # process_folder(idx, features, input_folder, output_folder)
    #
    # # Tropical_Forests_EF
    # path = 'Tropical_Forests_EF'
    # input_folder = os.path.join(base_input_folder, path)
    # output_folder = os.path.join(base_output_folder, path)
    # process_folder(idx, features, input_folder, output_folder)
    #
    # # CH4_Emissions_Burning_ClosedShrublands/
    # path = 'CH4_Emissions_Burning_ClosedShrublands'
    # input_folder = os.path.join(base_input_folder, path)
    # output_folder = os.path.join(base_output_folder, path)
    # process_folder(idx, features, input_folder, output_folder)
    #
    # # CH4_Emissions_Burning_Grasslands
    # path = 'CH4_Emissions_Burning_Grasslands'
    # input_folder = os.path.join(base_input_folder, path)
    # output_folder = os.path.join(base_output_folder, path)
    # process_folder(idx, features, input_folder, output_folder)
    #
    # # CH4_Emissions_Burning_HumidTropicalForests
    # path = 'CH4_Emissions_Burning_HumidTropicalForests'
    # input_folder = os.path.join(base_input_folder, path)
    # output_folder = os.path.join(base_output_folder, path)
    # process_folder(idx, features, input_folder, output_folder)
    #
    # # GEZ2010
    # path = 'GEZ2010'
    # input_folder = os.path.join(base_input_folder, path)
    # output_folder = os.path.join(base_output_folder, path)
    # process_folder(idx, features, input_folder, output_folder)



