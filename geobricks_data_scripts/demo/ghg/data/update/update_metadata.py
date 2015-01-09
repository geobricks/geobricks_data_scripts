from geobricks_data_scripts.dev.utils.data_manager_util import get_data_manager

data_manager = get_data_manager()


# Update the dsd structure adding changing the wms_url and the datasource
def update_dsd_with_wms_and_datasource(wms_url,  datasource):

    layers = data_manager.metadata_manager.get_all_layers()
    print len(layers)
    for l in layers:
        dsd = l["dsd"]
        dsd["datasource"] = datasource
        print l["uid"], dsd
        # result = data_manager.metadata_manager.overwrite_dsd_rid(dsd)
        # print result
        # update_dsd_with_wms_and_datasource_by_uid(l["uid"], wms_url,  datasource)


def update_dsd_with_wms_and_datasource_by_uid(uid, wms_url,  datasource):
    layer = data_manager.metadata_manager.get_by_uid(uid)
    dsd = layer["dsd"]
    dsd["datasource"] = datasource
    result = data_manager.metadata_manager.overwrite_dsd_rid(dsd)
    print result



update_dsd_with_wms_and_datasource("http://fenix.fao.org/geoserver", "geoserver")
# update_dsd_with_wms_and_datasource_by_uid("mod13a2", "http://fenix.fao.org/geoserver", "geoserver")