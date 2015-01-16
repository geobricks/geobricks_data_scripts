# coding=utf-8
import glob
import calendar
import datetime
import json
import os

from geobricks_data_scripts.utils.filesystem import get_filename
from geobricks_common.core.date import get_daterange
from geobricks_data_scripts.demo.utils.data_manager_util import get_data_manager

# data manager
data_manager = get_data_manager()


def create_metadata(title, product, date=None, default_style=None, map_projection_code="EPSG:3857", workspace="ghg", uid_distribution=None, is_raster=True, uid=None):

    metadata_def = {
        "title": {
            "EN": title["EN"] if "EN" in title else title,
            "ES": title["ES"] if "ES" in title else title,
            "FR": title["FR"] if "FR" in title else title
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
                # "coverageTime": {
                #     "to": from_date,
                #     "from": to_date
                # }
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
            "workspace": data_manager.geoserver_manager.get_default_workspace_name() if workspace is None else workspace,
            # "layerName": "layername",
            "layerName": sanitize_name(title["EN"] if "EN" in title else title),
            }
    }

    # get date range
    if date is not None:
        from_date, to_date = get_daterange(date)
        metadata_def["meContent"]["seCoverage"]["coverageTime"] = {"from": from_date, "to": to_date }



    if default_style is not None:
        metadata_def["dsd"]["defaultStyle"] = default_style

    # TODO: add uid_distribution id

    return metadata_def


def sanitize_name(name):
    """
    This method clean the name of a layer, should be avoided to use dots as names
    :param name: name of the layer
    :return: sanitized layer name
    """
    name = name.replace(".", "")
    name = name.replace(" ", "_")
    name = name.lower()
    return name



def publish_maghg(input_folder):
    input_files = glob.glob(input_folder + "/*.tif")

    # filename
    for input_file in input_files:
        # this if is for the layer's products conding system issues of the filenames
        # please see coding_system/publish_maghg_cs.py for the "IF" meaning
        date = None
        if "_3857" in input_file:
            projection_name = "EPSG:3857"

            if "20" in input_file or "19" in input_file:
            # it contains a date
                folder, filename = os.path.split(input_file.rsplit("_", 1)[0])
                folder, product = os.path.split(input_file.rsplit("_", 2)[0])
                date = input_file.rsplit("_", 2)[1]
            else:
                folder, filename = os.path.split(input_file.rsplit("_", 1)[0])
                folder, product = os.path.split(input_file.rsplit("_", 1)[0])

            product = product.lower()
            title = filename.replace("_", " ")
            sldname = get_sldname(filename)
            metadata_def = create_metadata(title, product, date, sldname, projection_name)
            try:
                # print product, json.dumps(metadata_def["dsd"]["layerName"])

                # delete if import failed
                #uid = metadata_def["dsd"]["workspace"] + ":" + metadata_def["dsd"]["layerName"]
                #data_manager.delete(metadata_def["dsd"]["workspace"] + ":" + metadata_def["dsd"]["layerName"])


                #  fix of some styles
                # if "n2o_ef" not in metadata_def["dsd"]["layerName"] and "n2o" in metadata_def["dsd"]["layerName"]:
                #     print metadata_def["dsd"]["layerName"]
                #     data_manager.geoserver_manager.set_style(metadata_def["dsd"]["layerName"], sldname)

                # upload
                data_manager.publish_coveragestore(input_file, metadata_def, False, True, True)
            except Exception, e:
                print e


def get_sldname(filename):
    sldname = "ghg_"
    if "FUELBIOMASS" in filename.upper():
        sldname = sldname + "fuelbiomass"
    elif "CH4_EF" in filename.upper():
        sldname = sldname + "ch4_ef"
    elif "CO2_EF" in filename.upper():
        sldname = sldname + "co2_ef"
    elif "N2O_EF" in filename.upper():
        sldname = sldname + "n2o_ef"
    elif "CH4" in filename.upper():
        sldname = sldname + "ch4"
    elif "CO2" in filename.upper():
        sldname = sldname + "co2"
    elif "DM" in filename.upper():
        sldname = sldname + "dm"

    elif "N2O" in filename.upper():
        sldname = sldname + "n2o"
    return sldname + "_EN"


# Publishing data
publish_maghg("/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/MAGHG-data/OUTPUT/")
