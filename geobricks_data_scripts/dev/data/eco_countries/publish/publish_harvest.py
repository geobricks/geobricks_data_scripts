import glob
import os
from geobricks_data_scripts.dev.utils.data_manager_util import get_data_manager
from geobricks_data_scripts.utils.harvest.publish_harvest import harvest_folder, update_folder_style


data_manager = get_data_manager()

lang = "EN"
workspace = "eco_countries"

metadatas = harvest_folder(data_manager, "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD16/ET/ET/ET_AVG/", workspace, True, False, False, None)
print metadatas
# harvest_folder(data_manager, "/home/vortex/Desktop/LAYERS/earthstat/earthstat_processeddata/geoserver/earthstat_crop_yield/", workspace)