from geobricks_data_scripts.prod.utils.data_manager_util import get_data_manager

data_manager = get_data_manager()
layers = data_manager.get_all_layers()
for layer in layers:
    try:
        #print layer["uid"]
        #data_manager.delete(layer["uid"])
        if "gfed4_burnedarea_humidtropicalforests_" in layer["uid"]:
            print layer["uid"]
            #data_manager.delete(layer["uid"])
    except Exception, e:
        print e
        pass