import glob
import os
from geobricks_common.core.filesystem import get_filename
from geobricks_data_scripts.dev.utils.data_manager_util import get_data_manager
from geobricks_data_scripts.utils.harvest.publish_harvest import harvest_folder, update_folder_style


data_manager = get_data_manager()

lang = "EN"
workspace = "ghg"

def get_maghg_defaultstyle_name(filename):
    sldname = ""
    if "FUELBIOMASS" in filename.upper():
        sldname = "fuelbiomass"
    elif "CH4_EF" in filename.upper():
        sldname = "ch4_ef"
    elif "CO2_EF" in filename.upper():
        sldname = "co2_ef"
    elif "N2O_EF" in filename.upper():
        sldname = "n2o_ef"
    elif "CH4" in filename.upper():
        sldname = "ch4"
    elif "CO2" in filename.upper():
        sldname = "co2"
    elif "DM" in filename.upper():
        sldname = "dm"
    elif "N2O" in filename.upper():
        sldname = "n2o"
    return sldname + "_emissions_burning_" + lang

# harvest_folder(data_manager, "/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/Theory_structure_novemeber_13/Cultivation_organic_soils_croplands/Cultivation_organic_soils_-_croplands/", workspace)
# harvest_folder(data_manager, "/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/Theory_structure_novemeber_13/GriddedLivestock/gridded_livestock_of_the_world_v_201/", workspace)
# harvest_folder(data_manager, "/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/Theory_structure_novemeber_13/JRC_CLIMATE_ZONE/JRC_climate_zone/", workspace)
# harvest_folder(data_manager, "/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/Theory_structure_novemeber_13/GLC2000/glc2000_v1/", workspace)
# harvest_folder(data_manager, "/home/vortex/Deskt/op/LAYERS/GHG_13_NOVEMEBRE/Theory_structure_novemeber_13/GEZ/global_ecological_zones_GEZ/", workspace)


def harvest_burned_areas(src_folder, output_folder="output", ):
    print "TODO:"

# GHG-MAG
# 4326
def harvest_maghg_4326():
    maghg_4326_folder = "/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/MAGHG-data/OUTPUT/storage"
    folders = glob.glob(os.path.join(maghg_4326_folder, "*"))
    for folder in folders:
        if os.path.isdir(folder):
            harvest_folder(data_manager, folder, workspace)

# 3857
def harvest_maghg_3857():
    maghg_3857_folder = "/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/MAGHG-data/OUTPUT/geoserver"
    folders = glob.glob(os.path.join(maghg_3857_folder, "*"))
    for folder in folders:
        if os.path.isdir(folder):
            harvest_folder(data_manager, folder, workspace)


def harvest_maghg_3857_updated_defaultstyle():
    maghg_3857_folder = "/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/MAGHG-data/OUTPUT/geoserver"
    folders = glob.glob(os.path.join(maghg_3857_folder, "*"))
    all_metadatas = []
    for folder in folders:
        if os.path.isdir(folder):
            all_metadatas.append(harvest_folder(data_manager, folder, workspace, False, False, False))

    # update the metadata retrieved
    for metadatas in all_metadatas:
        for metadata in metadatas:
            try:
                print metadata["dsd"]["layerName"]
                default_style = get_maghg_defaultstyle_name(metadata["dsd"]["layerName"])
                data_manager.geoserver_manager.set_style(metadata["dsd"]["layerName"], default_style)
            except Exception, e:
                print "ERRRROOOOO!!!!!"
                print e


# def create_storage_json_metadata(src_folder, code, product_codelist_id="layers_products"):
#     for glob=glob
#
#
# def create_product_json(code, product_codelist_id="layers_products"):
#     metadata = {
#         "meContent" : {
#             "seCoverage" : {
#                 "coverageSectors" : {
#                     "version" : "1.0",
#                     "codes" : [ {
#                                     "code" : code
#                                 } ],
#                     "idCodeList" : product_codelist_id
#                 }
#             }
#         }
#     }
#     return metadata



# DIRTY PRODUCT FIX
# def update_maghg_4326_storage_product(folder, workspace):
#     # there is an issue with the product code of the 4326 layers (they need to be update with the 3857 relative one)
#     folders = glob.glob(os.path.join(folder, "*"))
#     for folder in folders:
#         if os.path.isdir(folder):
#             files = glob.glob(os.path.join(folder, "*.geotiff"))
#             for f in files:
#                 uid = workspace + ":"
#                 uid += "_".join(get_filename(f).lower().split("_")[:-1]) + "_3857"
#                 print uid
#                 try:
#                     metadata = data_manager.metadata_manager.get_by_uid(uid)
#                     print metadata["dsd"]["contextExtension"]["distribution"][0]["uid"]
#                 except Exception, e:
#                     print "ERROR: ", e

    #data_manager.metadata_manager.update_metadata()



#harvest_maghg_4326()
#harvest_maghg_3857()
#harvest_maghg_3857_updated_defaultstyle()

# maghg_4326_folder = "/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/MAGHG-data/OUTPUT/storage"
# update_maghg_4326_storage_product(maghg_4326_folder, workspace)


