
from geobricks_data_scripts.dev.utils.data_manager_util import get_data_manager

data_manager = get_data_manager()
layers = data_manager.get_all_layers()
print "layers"
for layer in layers:
    try:
        if "eco_countries" in layer["dsd"]["workspace"]:
            data_manager.delete(layer["uid"])
            #print layer["uid"]
    except Exception, e:
        #print "Error", e
        pass