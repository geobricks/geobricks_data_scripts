
from geobricks_data_scripts.prod.ghg.utils.data_manager_util import get_data_manager

# data_manager = get_data_manager()
# layers = data_manager.get_all_layers()
# for layer in layers:
#     try:
#
#         print layer["uid"], layer["meContent"]["seCoverage"]["coverageSectors"]["codes"][0]
#         #data_manager.delete(layer["uid"])
#     except Exception, e:
#         print e
#         pass


import glob
import os
folders = glob.glob("/home/vortex/Desktop/LAYERS/ghg/download/4326/Burned_dry_matter/faostat/*")
countries = []
for f in folders:
    countries.append(os.path.basename(os.path.normpath(f)))

print countries