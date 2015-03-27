import calendar
import datetime
from geobricks_common.core.log import logger

log = logger(__file__)


def create_metadata(metadata):
    log.info(metadata)

    map_projection_code = str(metadata["map_projection_code"])
    product_codelist_id = "layers_products" if "product_codelist_id" not in metadata else metadata["layers_products"]
    product_codelist_version = "1.0" if "product_codelist_version" not in metadata else metadata["product_codelist_version"]

    metadata_def = {
        "title": metadata["title"],
        "creationDate": calendar.timegm(datetime.datetime.now().timetuple()) * 1000,
        "meContent": {
            "resourceRepresentationType": "geographic",
            "seCoverage": {}
        },

        "meSpatialRepresentation": {
            "layerType": "raster" if metadata["is_raster"] else "vector"
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
            "layerName": metadata["layerName"]
        }
    }

    # workspace
    if "workspace" in metadata:
        metadata_def["dsd"]["workspace"] = metadata["workspace"]

    # product
    if "product_code" in metadata:
        metadata_def["meContent"]["seCoverage"]["coverageSectors"] = {
            "idCodeList": product_codelist_id,
            "version": product_codelist_version,
            "codes": [{"code": metadata["product_code"]}]
        }

    # get date range
    if "from_date" in metadata:
        metadata_def["meContent"]["seCoverage"]["coverageTime"] = {"from": metadata["from_date"], "to": metadata["to_date"] }

    if "defaultStyle" in metadata:
        metadata_def["dsd"]["defaultStyle"] = metadata["defaultStyle"]

    return metadata_def



# def relate_metadata(metadata_config,  ):
    



# def _create_metadata(title, layerName=None, product=None, product_codelist_id="layers_products", product_codelist_version="1.0", from_date=None, to_date=None, workspace=None, default_style=None, map_projection_code="EPSG:3857", is_raster=True, lang="EN"):
#     metadata_def = {
#         "title": {
#             lang: title[lang] if lang in title else title,
#         },
#         "creationDate": calendar.timegm(datetime.datetime.now().timetuple()) * 1000,
#         "meContent": {
#             "resourceRepresentationType": "geographic",
#             "seCoverage": {}
#         },
#
#         "meSpatialRepresentation": {
#             "layerType": "raster" if is_raster else "vector"
#         },
#         "meReferenceSystem": {
#             "seProjection": {
#                 "projection": {
#                     "idCodeList": "mapProjections",
#                     "version": "1.0",
#                     "codes": [{"code": map_projection_code}]
#                 }
#             }
#         },
#         "dsd": {
#             "contextSystem": "FENIX",
#             #"workspace": data_manager.geoserver_manager.get_default_workspace_name() if workspace is None else workspace,
#             # "layerName": "layername",
#             "layerName": layerName,
#         }
#     }
#
#     # workspace
#     if workspace is not None:
#         metadata_def["dsd"]["workspace"] = workspace
#
#     # product
#     if product is not None:
#         metadata_def["meContent"]["seCoverage"]["coverageSectors"] = {
#             "idCodeList": product_codelist_id,
#             "version": product_codelist_version,
#             "codes": [{"code": product}]
#         }
#
#     # get date range
#     if from_date is not None:
#         metadata_def["meContent"]["seCoverage"]["coverageTime"] = {"from": from_date, "to": to_date }
#
#     if default_style is not None:
#         metadata_def["dsd"]["defaultStyle"] = default_style
#
#     return metadata_def
