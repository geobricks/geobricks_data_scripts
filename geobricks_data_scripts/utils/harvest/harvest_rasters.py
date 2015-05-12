import os
import glob
import pyproj
import datetime
import simplejson
from geobricks_common.core.log import logger
from geobricks_common.core.filesystem import get_filename, get_file_extension
from geobricks_common.core.date import get_daterange
from geobricks_common.core.filesystem import sanitize_name
from geobricks_data_scripts.utils.metadata.metadata import create_metadata
from geobricks_gis_raster.core.raster import get_authority
from geobricks_common.core.utils import dict_merge

log = logger(__file__)

language = "EN"

supported_file = ["tif", "tiff", "geotiff", "TIFF", "TIF", "GEOTIFF"]


def harvest_raster_folder(path, publish_metadata=True, publish_geoserver=True, publish_storage=True):
    # read files
    metadatas = []
    files = glob.glob(os.path.join(path, "*"))

    # getting product code from the folder name
    product_code = sanitize_name(os.path.basename(os.path.normpath(path)))

    for f in files:
        if os.path.isfile(f):
            metadata = None
            # sanitize file name?
            filename = get_filename(f)
            extension = get_file_extension(f)

            # check if is not a json
            if extension in supported_file and extension is not "json":
                log.info(filename)
                metadata = parse_filename(filename, get_authority(f).upper(), product_code)
                metadata = create_metadata(metadata)

                # check metadata .json (if exists for the file) with or without projections code at the end
                metadata_file_prj = os.path.join(path, filename + ".json")
                if os.path.isfile(metadata_file_prj):
                    with open(metadata_file_prj) as m_file:
                        d = simplejson.load(m_file)
                        metadata = dict_merge(metadata, d)

                metadata_file = os.path.join(path, "_".join(filename.split("_")[:(len(filename.split("_"))-1)]) + ".json")
                if os.path.isfile(metadata_file):
                    with open(metadata_file) as m_file:
                        d = simplejson.load(m_file)
                        metadata = dict_merge(metadata, d)



            if metadata:
                metadata["path"] = f
                metadatas.append(metadata)
    return metadatas


# the product_code is usually gived by the folder name
def parse_filename(filename, map_projection_code, product_code=None):
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
    if product_code is None:
        product_code = sanitize_name(' '.join(s))
    else:
        product_code = sanitize_name(product_code)

    product_label = sanitize_name(' '.join(s))
    sanitized_title = sanitize_name(title) + "_" + prj

    layerName = sanitized_title

    # it is gived by the product (TOdO: should it be common by all the layers?)
    defaultStyle = product_code + "_" + language.upper()

    print "Harvest raster:"
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

# TODO: check prj
def check_prj(prj):
    #print "Check if prj is valid"
    return True

