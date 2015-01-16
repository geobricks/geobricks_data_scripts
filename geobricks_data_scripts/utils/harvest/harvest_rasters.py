import os
import glob
import pyproj
import datetime
from geobricks_common.core.log import logger
from geobricks_common.core.filesystem import get_filename, get_file_extension
from geobricks_common.core.date import get_daterange
from geobricks_common.core.filesystem import sanitize_name
from geobricks_data_scripts.utils.metadata.metadata import create_metadata
from geobricks_gis_raster.core.raster import get_authority

log = logger(__file__)

language = "EN"

supported_file = ["tif", "tiff", "geotiff", "TIFF", "TIF", "GEOTIFF"]

metadata_file = ["json"]


def harvest_raster_folder(path, workspace=None):
    # read files
    files = glob.glob(os.path.join(path, "*"))
    for f in files:
        # sanitize file name?
        filename = get_filename(f)
        extension = get_file_extension(f)
        if extension in supported_file:
            log.info(filename)
            metadata = parse_filename(filename, get_authority(f).upper())
            metadata = create_metadata(metadata)

            # check if exists a file named like the "file".json ( and in case overwrite the what is used there)
            #metadata_file =
            print metadata

        if extension in metadata_file:
            log.info(filename)


def parse_filename(filename, map_projection_code):
    # get name, date, proj
    filename = filename
    s = filename.split("_")
    prj = s[len(s)-1]

    # check if the last part is the prj
    if check_prj(prj):
        s.remove(prj)

    # title
    title = ' '.join(s)

    # initialize dates
    fromdate = None
    todate = None

    # check dates
    if len(s) > 1:
        date = s[len(s)-1]
        fromdate, todate = get_daterange(date)
        if fromdate is not None and todate is not None:
            s.remove(date)

    # product (in case it skips the date)
    product_code = sanitize_name(' '.join(s))
    product_label = sanitize_name(' '.join(s))
    sanitized_title = sanitize_name(title)

    layerName = sanitized_title

    # it is gived by the product (TOdO: should it be common by all the layers?)
    defaultStyle = product_code + "_" + language.upper()

    print "-------------"
    print title, product_code, product_label, layerName, defaultStyle, fromdate, todate, prj

    metadata = {
        "title": {
            language: title
        },
        "product_code": product_code,
        "product_label": product_label,
        "layerName": layerName,
        "defaultStyle": defaultStyle,
        "map_projection_code": map_projection_code,
        "is_raster": True,
    }

    # dates
    if fromdate is not None:
        metadata["from_date"] = fromdate
        metadata["to_date"] = todate

    return metadata

def check_prj(prj):
    print "Check if prj is valid or is the name"



harvest_raster_folder("/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/Theory_structure_novemeber_13/Cultivation_organic_soils_croplands/publish/")
