import glob
import os
from geobricks_data_scripts.prod.ghg.utils.data_manager_util import get_data_manager
from geobricks_data_scripts.utils.harvest.publish_harvest import harvest_folder


data_manager = get_data_manager()

lang = "EN"
workspace = "earthstat"


metadatas = harvest_folder(data_manager, "/home/vortex/Desktop/LAYERS/earthstat/TO_PUBLISH/earthstat_crop_area/", workspace)
print metadatas
# harvest_folder(data_manager, "/home/vortex/Desktop/LAYERS/earthstat/earthstat_processeddata/geoserver/earthstat_crop_yield/", workspace)


