from geobricks_common.core.log import logger
from geobricks_data_scripts.utils.harvest.harvest_rasters import harvest_raster_folder

log = logger(__file__)


# TODO: apply publish on storage and geoserver
def harvest_folder(data_manager, folder, workspace, publish_on_geoserver=True, publish_on_storage=True, update_links=True, metadata_json=None):
    metadatas = harvest_raster_folder(folder)
    print metadatas

    # harvest 3857 for publication
    for metadata in metadatas:
        log.info(metadata)
        # check epsg
        if metadata["meReferenceSystem"]["seProjection"]["projection"]["codes"][0]["code"] == "EPSG:3857":
            if "workspace" not in metadata["dsd"]:
                metadata["dsd"]["workspace"] = workspace
            if publish_on_geoserver:
                metadata = publish_geoserver(data_manager, metadata["path"], metadata)
                log.info(metadata)


    # harvest 4326 (or others) to storage
    # it's done after the 3857 it's sure the metadata will be there
    for metadata in metadatas:
        log.info(metadata)
        if metadata["meReferenceSystem"]["seProjection"]["projection"]["codes"][0]["code"] != "EPSG:3857":
            if publish_on_storage:
                metadata = publish_storage(data_manager, metadata["path"], metadata, workspace)
                log.info(metadata)

    log.info(metadatas)
    if update_links:
        # link 3857 layer to 4326 distribution layer
        for metadata in metadatas:
            log.info(metadata)
            # check epsg
            if metadata["meReferenceSystem"]["seProjection"]["projection"]["codes"][0]["code"] == "EPSG:3857":
                # TODO: get code
                update_dsd_layer_to_distribution_layer(data_manager, metadata)


        # link 4326 (or other Proj EPSG) layer to 3857 visualization layer
        for metadata in metadatas:
            log.info(metadata)
            # check epsg
            if metadata["meReferenceSystem"]["seProjection"]["projection"]["codes"][0]["code"] != "EPSG:3857":
                # TODO: get code
                update_dsd_layer_to_visualization_layer(data_manager, metadata, workspace)
    return metadatas


def update_folder_style(data_manager, folder, style=None):
    '''
    Updates all layer style in the folder.
    the basic defaultStlye is taken by the layer name minus the date (if used) and the prj
    :param data_manager:
    :param folder:
    :param style:
    :return:
    '''
    metadatas = harvest_raster_folder(folder)
    for metadata in metadatas:
        if metadata["meReferenceSystem"]["seProjection"]["projection"]["codes"][0]["code"] == "EPSG:3857":
            print metadata["dsd"]
            try:
                if style is not None:
                    data_manager.geoserver_manager.set_style(metadata["dsd"]["layerName"], style)
                else:
                    data_manager.geoserver_manager.set_style(metadata["dsd"]["layerName"], metadata["dsd"]["defaultStyle"])
            except Exception, e:
                log.warn(e)



def update_dsd_layer_to_distribution_layer(data_manager, metadata, epsg_code):
    log.info(metadata)
    update_dsd_layer_with_layer_dist_or_vis(data_manager, metadata["uid"], epsg_code, "distribution")
    #update_dsd_layer_with_layer_dist_or_vis(data_manager, metadata["uid"], "4326", "distribution")


def update_dsd_layer_to_visualization_layer(data_manager, metadata, workspace, epsg_code):
    log.info(metadata)
    update_dsd_layer_with_layer_dist_or_vis(data_manager, metadata["uid"], epsg_code, "visualization", workspace)
    #update_dsd_layer_with_layer_dist_or_vis(data_manager, metadata["uid"], "3857", "visualization", workspace)


def publish_geoserver(data_manager, path, metadata):
    log.info("publish on geoserver")
    try:
        return data_manager.publish_coveragestore(path, metadata)
    except Exception, e:
        log.error(e)


def publish_storage(data_manager, path, metadata, workspace=None, uid_distribution=True):
    log.info("publish on storage")
    try:
        return data_manager.publish_coveragestore_storage(path, metadata, False, False, True)
    except Exception, e:
        log.error(e)


def update_dsd_layer_with_layer_dist_or_vis(data_manager, uid, epsg_code="4326", type="distribution", workspace=None):
    try:
        metadata = data_manager.get_metadata_by_uid(uid)
        # TODO this should be done through layername and workspace
        layer_uid = ""
        if workspace:
            layer_uid += workspace + ":"
        layer_uid += "_".join(metadata["dsd"]["layerName"].split("_")[:-1]) + "_" + epsg_code
        print layer_uid
        metadata_layer = data_manager.get_metadata_by_uid(layer_uid)
        print metadata_layer

        # add distribution uid
        if "contextExtension" not in metadata["dsd"]:
            metadata["dsd"]["contextExtension"] = {}

        obj = {
            "uid":  metadata_layer["uid"]
        }
        if "version" in metadata_layer:
            obj["version"] = metadata_layer["version"]

        # TODO: replace or append? (there should be a policy)
        # TODO: For now it's overwrite!
        # if type not in metadata["dsd"]["contextExtension"]:
        #     metadata["dsd"]["contextExtension"][type] = []
        # metadata["dsd"]["contextExtension"][type].append(obj)
        metadata["dsd"]["contextExtension"][type] = [obj]

        # update dsd
        dsd = metadata["dsd"]
        print "UPDATE", dsd
        result = data_manager.metadata_manager.overwrite_dsd_rid(dsd)
        print result

    except Exception, e:
        # log.error("No metadata found for ", str(layer_uid))
        log.error(e)


