from geobricks_data_scripts.demo.utils.data_manager_util import get_data_manager

data_manager = get_data_manager()


# Update the dsd structure adding changing the wms_url and the datasource
def update_dsd_with_wms_and_datasource(wms_url,  datasource):

    layers = data_manager.metadata_manager.get_all_layers()
    for l in layers:
        metadata = data_manager.metadata_manager.get_by_uid(l["uid"])
        print metadata["dsd"]
        break


update_dsd_with_wms_and_datasource("http://fenix.fao.org/geoserver", "geoserver")