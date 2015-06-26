from geobricks_data_scripts.demo.fenix.utils.data_manager_util import get_data_manager

data_manager = get_data_manager()
layers = data_manager.get_all_layers()
print "layers"
for layer in layers:
    try:
        if "myd11c3_anomaly" in layer["dsd"]["workspace"]:
            print layer["uid"]
            #data_manager.delete(layer["uid"])
    except Exception, e:
        #print "Error", e
        pass