# coding=utf-8
import glob
import calendar
import datetime
import json

from geobricks_data_scripts.utils.filesystem import get_filename
from geobricks_common.core.date import get_daterange
from geobricks_data_scripts.demo.utils.data_manager_util import get_data_manager
#  data manger
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
                }
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


def publish_data_GriddedLivestock(input_folder):
    input_files = glob.glob(input_folder +"/*.tif")
    product = "Gridded Livestock of the World v. 2.01"
    for input_file in input_files:
        info = str.split(get_filename(input_file), "_")
        title = info[0].capitalize() + " " + info[1] + " - " + info[2]
        sldname = "ghg_" + get_filename(input_file).lower() + "_EN"
        date = info[2]
        metadata_def = create_metadata(title, product, date, sldname)
        try:
            print json.dumps(metadata_def)
            data_manager.publish_coveragestore(input_file, metadata_def, False, False, True)
        except Exception, e:
            print e
        #manager.publish_coverage(input_file, metadata_def, False, False)


def publish_data_Climate_Zones_processed(input_folder):
    input_files = glob.glob(input_folder +"/*.tif")
    product = "JRC climate zone"
    sldname = "ghg_jrc_climate_zone_0.25deg" + "_EN"
    for input_file in input_files:
        info = str.split(get_filename(input_file), "_")
        title = info[0] + " " + info[1].lower() + " - " + info[2].lower()
        map_projection_code = "EPSG:3857"
        if "4326" in info[4]:
            title += " (4326)"
            product += " (4326)"
            map_projection_code = "EPSG:4326"
        date = "2010"
        metadata_def = create_metadata(title, product, date, sldname, map_projection_code)
        try:
            print json.dumps(metadata_def)
            data_manager.publish_coveragestore(input_file, metadata_def, False, False, True)
        except Exception, e:
            print e
        #manager.publish_coverage(input_file, metadata_def, False, False)


def publish_data_modis_landcover(input_folder):
    input_files = glob.glob(input_folder +"/*.tif")
    product = "MODIS - Land Cover Type UMD"
    sldname = "modis_land_cover" + "_EN"
    for input_file in input_files:
        info = str.split(get_filename(input_file), "_")
        title = info[0] + " " + info[1] + " " + info[2] + " " + info[3] + " " + info[4] + " " + info[5] + " - " + info[6]
        map_projection_code = "EPSG:3857"
        if "4326" in info[4]:
            title += " (4326)"
            product += " (4326)"
            map_projection_code = "EPSG:4326"
        date = info[6]
        metadata_def = create_metadata(title, product, date, sldname, map_projection_code)
        try:
            print json.dumps(metadata_def)
            data_manager.publish_coveragestore(input_file, metadata_def, False, False, True)
        except Exception, e:
            print e
        #manager.publish_coverage(input_file, metadata_def, False, False)


def publish_burnerdareas():
    path = "/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/GFED4_BURNEDAREAS_BY_LANDCOVER/"
    input_dir = glob.glob(path + "*")
    for d in input_dir:
        input_files = glob.glob(d + "/*.tiff")

        # sld and workspace
        sldname = "ghg_burnedareas" + "_EN"
        workspace = "fenix:"

        for input_file in input_files:
            #print input_file
            if "3857" in input_file:
                if "humid" in input_file.lower() or "allforests" in input_file.lower():
                    print input_file
                    info = str.split(get_filename(input_file), "_")
                    date = info[3]
                    filename = get_filename(input_file).rsplit('_', 1)[0]
                    uid = workspace + get_filename(filename).lower()
                    product = burned_areas_switch(filename)
                    title = product + " " + info[3]
                    metadata_def = create_metadata(title, product, date, sldname)
                    try:
                        print json.dumps(metadata_def)
                        data_manager.publish_coveragestore(input_file, metadata_def, False, False, True)
                    except Exception, e:
                        print e
                    #manager.publish_coverage(input_file, metadata_def, False, False)
                else:
                    info = str.split(get_filename(input_file), "_")
                    date = info[4]
                    filename = get_filename(input_file).rsplit('_', 1)[0]
                    uid = workspace + get_filename(filename).lower()
                    product = burned_areas_switch(input_file)
                    title = product + " " + info[4]
                    metadata_def = create_metadata(title, product, date, sldname)
                    try:
                        print json.dumps(metadata_def)
                        data_manager.publish_coveragestore(input_file, metadata_def, False, False, True)
                    except Exception, e:
                        print e
                    #manager.publish_coverage(input_file, metadata_def, False, False)
            else: #4326
                info = str.split(get_filename(input_file), "_")
                if len(info) >= 5:
                    title = info[0] + " " + info[1] + " " + info[2] + " " + info[3] + " " + info[4] + " - 4326"
                    date = info[4]
                else:
                    title = info[0] + " " + info[1] + " " + info[2] + " " + info[3]
                    date = info[3]
                product = get_filename(input_file).replace('_', ' ') + " (4326)"
                metadata_def = create_metadata(title, product, date, sldname)
                try:
                    print json.dumps(metadata_def)
                    data_manager.publish_coveragestore(input_file, metadata_def, False, False, True)
                except Exception, e:
                    print e


def burned_areas_switch(filename):
    filename = filename.lower()
    if "peatlands" in filename:
        return "GFED4 Burned Areas - Organic soils"
    if "AllForestsMinus".lower() in filename:
        return "GFED4 Burned Areas - Other forest"
    if "humidtropicalforests".lower() in filename:
        return "GFED4 Burned Areas - Humid Tropical Forest"

    burned_areas_lc = "GFED4 Burned Areas - "
    if "lc_1_" in filename:
        return burned_areas_lc + "Evergreen Needleleaf forest"
    if "lc_2_" in filename:
        return burned_areas_lc + "Evergreen Broadleaf forest"
    if "lc_3_" in filename:
        return burned_areas_lc + "Deciduous Needleleaf forest"
    if "lc_4_" in filename:
        return burned_areas_lc + "Deciduous Broadleaf forest"
    if "lc_5_" in filename:
        return burned_areas_lc + "Mixed forest"
    if "lc_6_" in filename:
        return burned_areas_lc + "Closed shrubland"
    if "lc_7_" in filename:
        return burned_areas_lc + "Open shrubland"
    if "lc_8_" in filename:
        return burned_areas_lc + "Woody savanna"
    if "lc_9_" in filename:
        return burned_areas_lc + "Savanna"
    if "lc_10_" in filename:
        return burned_areas_lc + "Grassland"
    if "lc_12_" in filename:
        return burned_areas_lc + "Croplands"
    if "lc_13_" in filename:
        print filename
        return burned_areas_lc + "Urban and built-up"
    if "lc_16_" in filename:
        return burned_areas_lc + "Barren or sparsely vegetated"
    if "lc_17_" in filename:
        return burned_areas_lc + "Unclassified"


def publish_gez_vector():
    uid = "fenix:gez_2010_3857"
    title = "Global Ecological Zones (GEZ) 2010  - Vector"
    product = "Global Ecological Zones (GEZ) 2010"
    sldname = "ghg_gez_2010" + "_EN"
    date = "2010"
    metadata_def = create_metadata(title, product, date, sldname)
    print metadata_def
    #manager.publish_shapefile(None, metadata_def, False, False)

def publish_area_of_histosols(path):
    input_files = glob.glob(path + "*.tif")
    for input_file in input_files:
        title = "Organic soil surface area"
        product = "Harmonized World Soil Database - Organic soils"
        sldname = "ghg_area_of_histosols" + "_EN"
        date = '2008'
        metadata_def = create_metadata(title, product, date, sldname)
        try:
            print json.dumps(metadata_def)
            data_manager.publish_coveragestore(input_file, metadata_def, False, False, True)
        except Exception, e:
            print e


def publish_gez(path):
    input_files = glob.glob(path + "*.tif")
    for input_file in input_files:
        title = "Global Ecological Zones (GEZ) 2010 - Raster"
        product = "Global Ecological Zones (GEZ) 2010"
        sldname = "ghg_gez_2010_raster" + "_EN"
        date = '2010'
        metadata_def = create_metadata(title, product, date, sldname)
        try:
            print json.dumps(metadata_def)
            data_manager.publish_coveragestore(input_file, metadata_def, False, False, True)
        except Exception, e:
            print e


def publish_ghg_glc2000_v1_1(path):
    input_files = glob.glob(path + "*.tif")
    for input_file in input_files:
        title = "Global Land Cover 2000 (GLC2000)"
        product = "Global Land Cover 2000 (GLC2000)"
        sldname = "ghg_glc2000_v1_1" + "_EN"
        date = '2000'
        metadata_def = create_metadata(title, product, date, sldname)
        try:
            print json.dumps(metadata_def)
            data_manager.publish_coveragestore(input_file, metadata_def, False, False, True)
        except Exception, e:
            print e


def publish_cultivation_organic_soils_croplands(path):
    input_files = glob.glob(path + "*.tif")
    for input_file in input_files:
        #info = "Organic soil surface area"
        #uid = "fenix:gez_"
        title = "Cultivation Organic Soils - Croplands"
        product = "Cultivation Organic Soils"
        sldname = "ghg_cultivation_organic_soils_cropland" + "_EN"
        date = '2000'
        metadata_def = create_metadata(title, product, date, sldname)
        try:
            print json.dumps(metadata_def)
            data_manager.publish_coveragestore(input_file, metadata_def, False, False, True)
        except Exception, e:
            print e


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

# publish_data_GriddedLivestock("/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/GriddedLivestock/to_publish_3857/")
# publish_data_Climate_Zones_processed("/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/Climate_Zones_processed/to_publish/")
publish_data_modis_landcover("/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/MCD12Q1/processed_2009/3857/")
# publish_burnerdareas()
# publish_area_of_histosols("/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/HWSD/3857/")
# publish_gez("/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/gez_raster/3857/")
# publish_gez_vector()
# publish_ghg_glc2000_v1_1("/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/glc2000/3857/")
# publish_cultivation_organic_soils_croplands("/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/cultivation_organic_soils/3857/")

