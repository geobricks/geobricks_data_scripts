import os
import glob
from geobricks_common.core.log import logger
from geobricks_data_scripts.dev.utils.data_manager_util import get_data_manager
from geobricks_data_scripts.utils.harvest.publish_harvest import harvest_folder, update_folder_style

log = logger(__file__)

data_manager = get_data_manager()

workspace = "test"


def default_import(src_folder):
    log.info("GLC2000: " + src_folder)
    metadatas = harvest_folder(data_manager, src_folder, workspace, True, True, True)


def burned_areas(src_folder):
    folders = glob.glob(os.path.join(src_folder, "*"))
    for folder in folders:
        folder = os.path.join(folder, "output")
        log.info(folder)
        metadatas = harvest_folder(data_manager, folder, workspace, True, True, True)
        log.info(metadatas)
        for metadata in metadatas:
            log.info(metadata)
            if "3857" in metadata["dsd"]["layerName"]:
                log.info("here")
                # log.info"metadata["dsd"]["datasource"])
                data_manager.geoserver_manager.set_style(metadata["dsd"]["layerName"], workspace, "burned_areas_EN")


# used just to set the style to modis that was wrong
def set_style_modis():
    data_manager.geoserver_manager.set_style("modis_land_cover_mod12q1_umd_500m_2009_3857", workspace, "modis_-_land_cover_type_umd_EN")


if __name__ == '__main__':
    base_folder = "/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/Theory_structure_novemeber_13/TO_PUBLISH"

    #Cultivation organic soils
    #default_import(os.path.join(base_folder, "Cultivation_organic_soils_croplands", "Cultivation_organic_soils_-_croplands"))

    # Burned areas
    #burned_areas(os.path.join(base_folder, "GFED4_BURNEDAREAS_BY_LANDCOVER"))

    # GLC 2000
    #default_import(os.path.join(base_folder, "Global_Land_Cover_2000_(GLC_2000)", "Global_Land_Cover_2000_(GLC_2000)"))

    # griddedlivestock
    #default_import(os.path.join(base_folder, "GriddedLivestock", "gridded_livestock_of_the_world_v_201"))

    # JRC Climate zone
    #default_import(os.path.join(base_folder, "JRC_CLIMATE_ZONE", "JRC_climate_zone"))

    # MODIS_-_Land_Cover_type_UMD
    #default_import(os.path.join(base_folder, "MODIS_land_cover", "MODIS_-_Land_Cover_type_UMD"))



