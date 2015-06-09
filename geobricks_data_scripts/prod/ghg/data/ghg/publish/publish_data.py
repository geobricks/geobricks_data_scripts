import glob
import os
from geobricks_common.core.log import logger
from geobricks_data_scripts.prod.ghg.utils.data_manager_util import get_data_manager
from geobricks_data_scripts.utils.harvest.publish_harvest import harvest_folder

log = logger(__file__)

data_manager = get_data_manager()

workspace = "ghg"

def default_import(src_folder, defaultStyle=None):
    metadata_json = None
    if defaultStyle is not None:
        metadata_json = {
            "dsd": {
                "defaultStyle": defaultStyle
            }
        }
    harvest_folder(data_manager, src_folder, workspace, True, True, True, metadata_json)


def import_raster_3857():
    print "Import Raster 3857--------------------"
    base_folder = "/home/vortex/Desktop/LAYERS/ghg/geodata_handedoverto_simonem/3857_display_only/"

    # # CH4 Emissions Burning
    # default_import(base_folder + "CH4_Emissions_Burning_ClosedShrublands", "ch4_gfed4ba_emissions_burning_en")
    # default_import(base_folder + "CH4_Emissions_Burning_Grasslands", "ch4_gfed4ba_emissions_burning_en")
    # default_import(base_folder + "CH4_Emissions_Burning_HumidTropicalForests", "ch4_gfed4ba_emissions_burning_en")
    # default_import(base_folder + "CH4_Emissions_Burning_OtherForests", "ch4_gfed4ba_emissions_burning_en")
    # default_import(base_folder + "CH4_Emissions_Burning_Peatlands", "ch4_gfed4ba_emissions_burning_en")
    # default_import(base_folder + "CH4_Emissions_Burning_Savanna", "ch4_gfed4ba_emissions_burning_en")
    # default_import(base_folder + "CH4_Emissions_Burning_WoodySavanna", "ch4_gfed4ba_emissions_burning_en")
    #
    # # CO2 Emissions Burning
    # default_import(base_folder + "CO2_Emissions_Burning_ClosedShrublands", "co2_gfed4ba_emissions_burning_en")
    # default_import(base_folder + "CO2_Emissions_Burning_Grasslands", "co2_gfed4ba_emissions_burning_en")
    # default_import(base_folder + "CO2_Emissions_Burning_HumidTropicalForests", "co2_gfed4ba_emissions_burning_en")
    # default_import(base_folder + "CO2_Emissions_Burning_OtherForests", "co2_gfed4ba_emissions_burning_en")
    # default_import(base_folder + "CO2_Emissions_Burning_Peatlands", "co2_gfed4ba_emissions_burning_en")
    # default_import(base_folder + "CO2_Emissions_Burning_Savanna", "co2_gfed4ba_emissions_burning_en")
    # default_import(base_folder + "CO2_Emissions_Burning_WoodySavanna", "co2_gfed4ba_emissions_burning_en")
    #
    # # CO2_CultivationOrganicSoils (The layers have a json file for the style)
    # default_import(base_folder + "CO2_CultivationOrganicSoils")
    #
    # # CultivationOrganicSoils (The layers have a json file for the style)
    # default_import(base_folder + "CultivationOrganicSoils")
    #
    # # DM
    # default_import(base_folder + "DM_Burning_ClosedShrublands", "dm_gfed4_burning_en")
    # default_import(base_folder + "DM_Burning_Grasslands", "dm_gfed4_burning_en")
    # default_import(base_folder + "DM_Burning_HumidTropicalForests", "dm_gfed4_burning_en")
    # default_import(base_folder + "DM_Burning_OpenShrublands", "dm_gfed4_burning_en")
    # default_import(base_folder + "DM_Burning_OtherForests", "dm_gfed4_burning_en")
    # default_import(base_folder + "DM_Burning_OtherForests", "dm_gfed4_burning_en")
    # default_import(base_folder + "DM_Burning_Peatlands", "dm_gfed4_burning_en")
    # default_import(base_folder + "DM_Burning_Savanna", "dm_gfed4_burning_en")
    # default_import(base_folder + "DM_Burning_WoodySavanna", "dm_gfed4_burning_en")
    #
    # # FuelBiomass (The layers have a json file for the style)
    # default_import(base_folder + "FuelBiomass")
    #
    # # GEZ2010
    # default_import(base_folder + "GEZ2010")
    #
    # # GFED4 Burned Areas
    # default_import(base_folder + "GFED4_BurnedAreas_ClosedShrubland", "gfed4_burnedarea_en")
    # default_import(base_folder + "GFED4_BurnedAreas_DeciduousBroadleafForest", "gfed4_burnedarea_en")
    # default_import(base_folder + "GFED4_BurnedAreas_DeciduousNeedleleafForest", "gfed4_burnedarea_en")
    # default_import(base_folder + "GFED4_BurnedAreas_Deforestation", "gfed4_burnedarea_en")
    # default_import(base_folder + "GFED4_BurnedAreas_EvergreenBroadleafForest", "gfed4_burnedarea_en")
    # default_import(base_folder + "GFED4_BurnedAreas_EvergreenNeedleleafForest", "gfed4_burnedarea_en")
    # default_import(base_folder + "GFED4_BurnedAreas_Grassland", "gfed4_burnedarea_en")
    # default_import(base_folder + "GFED4_BurnedAreas_MixedForest", "gfed4_burnedarea_en")
    # default_import(base_folder + "GFED4_BurnedAreas_OpenShrubland", "gfed4_burnedarea_en")
    # default_import(base_folder + "GFED4_BurnedAreas_OtherForest", "gfed4_burnedarea_en")
    # default_import(base_folder + "GFED4_BurnedAreas_Peatlands", "gfed4_burnedarea_en")
    # default_import(base_folder + "GFED4_BurnedAreas_Savanna", "gfed4_burnedarea_en")
    # default_import(base_folder + "GFED4_BurnedAreas_WoodySavanna", "gfed4_burnedarea_en")
    default_import(base_folder + "GFED4_BurnedAreas_HumidTropicalForests", "gfed4_burnedarea_en")
    #
    # # GLC2000
    # default_import(base_folder + "GLC2000")
    #
    # # GriddedLivestock
    # default_import(base_folder + "GriddedLivestock", "griddedlivestock_heads_en")
    #
    # # HWSD
    # default_import(base_folder + "HWSD", "hwsd_histosols_area_en")
    #
    # # JRC_Climate
    # default_import(base_folder + "JRC_Climate", "jrc_climate_zones_en")
    #
    # # N2O
    # # N.B. "N2O_CultivationOrganicSoils" ha come stile "cultivation_organicsoils_n2o_emissions"
    # default_import(base_folder + "N2O_CultivationOrganicSoils", "cultivation_organicsoils_n2o_emissions_en")
    # default_import(base_folder + "N2O_Emissions_Burning_ClosedShrublands", "n2o_gfed4ba_emissions_burning_en")
    # default_import(base_folder + "N2O_Emissions_Burning_Grasslands", "n2o_gfed4ba_emissions_burning_en")
    # default_import(base_folder + "N2O_Emissions_Burning_HumidTropicalForests", "n2o_gfed4ba_emissions_burning_en")
    # default_import(base_folder + "N2O_Emissions_Burning_OpenShrublands", "n2o_gfed4ba_emissions_burning_en")
    # default_import(base_folder + "N2O_Emissions_Burning_OtherForests", "n2o_gfed4ba_emissions_burning_en")
    # default_import(base_folder + "N2O_Emissions_Burning_Peatlands", "n2o_gfed4ba_emissions_burning_en")
    # default_import(base_folder + "N2O_Emissions_Burning_Savanna", "n2o_gfed4ba_emissions_burning_en")
    # default_import(base_folder + "N2O_Emissions_Burning_WoodySavanna", "n2o_gfed4ba_emissions_burning_en")

    # # Burning Peatlands (The layers have a json file for the style)
    # default_import(base_folder + "Peatlands_EF")
    #
    # # Savanna+Grassland_EF (The layers have a json file for the style)
    # default_import(base_folder + "Savanna_and_Grassland_EF")
    #
    # # Emission Factor (The layers have a json file for the style)
    # default_import(base_folder + "Tropical_Forests_EF")
    #
    # # ExtraTropical_Forests_EF (The layers have a json file for the style)
    # default_import(base_folder + "ExtraTropical_Forests_EF")



def import_raster_4326():
    print "Import Raster 4326--------------------"
    base_folder = "/home/vortex/Desktop/LAYERS/ghg/geodata_handedoverto_simonem/4326/*"

    folders = glob.glob(base_folder)
    for folder in folders:
        if os.path.isdir(folder):
            harvest_folder(data_manager, folder, workspace, False, True, True)



if __name__ == '__main__':

    import_raster_3857()

    # import_raster_4326()
