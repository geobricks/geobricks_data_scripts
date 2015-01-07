# coding=utf-8
import glob
import calendar
import datetime
import json
import os
from geobricks_common.core.filesystem import sanitize_name, get_filename

from geobricks_data_scripts.utils.filesystem import get_filename
from geobricks_data_scripts.utils.date import get_range_dates_metadata_yearly
from geobricks_data_scripts.dev.utils.data_manager_util import get_data_manager

# data manager
data_manager = get_data_manager()


def create_metadata(title, product, date=None, default_style=None, map_projection_code="EPSG:4326", workspace=None, uid_distribution=None, is_raster=True, uid=None, datasource="storage"):

    metadata_def = {
        "title": {
            "EN": title["EN"] if "EN" in title else title,
        },
        "creationDate": calendar.timegm(datetime.datetime.now().timetuple()) * 1000,
        "meContent": {
            "resourceRepresentationType": "geographic",
            "seCoverage": {
                "coverageSectors": {
                    "idCodeList": "layer_products",
                    "version": "1.0",
                    "codes": [{"code": sanitize_name(product)}]
                },
            }
        },
        "meSpatialRepresentation": {
            "layerType": "raster" if is_raster else "vector"
        },
        "meReferenceSystem": {
            "seProjection": {
                "projection": {
                    "idCodeList": "mapProjections",
                    "version": "1.0",
                    "codes": [{"code": map_projection_code}]
                }
            }
        },
        "dsd": {
            "contextSystem": "FENIX",
            #"workspace": data_manager.geoserver_manager.get_default_workspace_name() if workspace is None else workspace,
            # "layerName": "layername",
            "layerName": sanitize_name(title["EN"] if "EN" in title else title),
        }
    }

    # get date range
    if date is not None:
        from_date, to_date = get_range_dates_metadata_yearly(date)
        metadata_def["meContent"]["seCoverage"]["coverageTime"] = {"from": from_date, "to": to_date }


    # storeType:
    metadata_def["dsd"]["datasource"] = datasource

    metadata_def["dsd"]["datasource"] = datasource

    # TODO: add uid_distribution id

    return metadata_def



def publish(input_folder):
    input_files = glob.glob(input_folder + "/*.geotiff")

    # filename
    for input_file in input_files:
        filename = get_filename(input_file)
        filename, projection_code = filename.split("_")
        projection_code = "EPSG:" + projection_code
        product = "test_storage"

        title = filename.replace("_", " ")
        metadata_def = create_metadata(title, product, None, None, projection_code, None, None, True, None, "storage")

        try:
            print metadata_def
            # upload
            data_manager.publish_coveragestore_storage(input_file, metadata_def, False, False, True)
        except Exception, e:
            print e


# Publishing data
publish("/home/vortex/Desktop/LAYERS/geobricks/storage/raster/mod13a2_3857/")
