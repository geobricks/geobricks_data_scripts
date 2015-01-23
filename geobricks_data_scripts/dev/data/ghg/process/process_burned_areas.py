import glob
import os
import shutil
from geobricks_common.core.log import logger
from geobricks_common.core.filesystem import get_filename
from geobricks_processing.core.processing_core import process_obj

log = logger(__file__)

output_extension = "geotiff"


process_obj_3857 = [
    {
        # "source_path": [source_path],
        # "output_path": output_path,
        # "output_file_name": "burundi_maize_area_4326.tif",
        "band": 1,
        "process": [
            {
                "gdal_translate": {
                    "opt": {
                        "-of": "GTiff",
                        "-a_nodata": "0",
                        "-a_srs": "EPSG:3857",
                        "-co": "'TILED=YES'",
                        "-co": "'COMPRESS=DEFLATE'",
                        }
                }
            },
        ]
    },
    {
        "band": 1,
        "process": [
            {
                "gdaladdo": {
                    "parameters": {
                        # "--config": "BIGTIFF_OVERVIEW IF_NEEDED"
                    },
                    "overviews_levels": "2 4 8 16"
                }
            }
        ]
    }
]


process_obj_4326 = [
    {
        "band": 1,
        "process": [
            {
                "gdal_translate": {
                    "opt": {
                        "-of": "GTiff",
                        "-a_nodata": "0",
                        "-a_srs": "EPSG:4326",
                        "-co": "'COMPRESS=DEFLATE'",
                        }
                }
            }
        ]
    }
]


def process(src_folder, dest_folder, file_type):
    # folders = glob.glob(os.path.join(src_folder, "*"))
    # for folder in folders:
    #     if os.path.isdir(folder):
            # dest_folder = create_output_folder(folder, folder_type, overwrite)
            output_path = create_output_folder(dest_folder)
            files = glob.glob(os.path.join(src_folder, "*." + file_type))
            for f in files:
                filename = get_filename(f)
                if "3857" in f:
                    prj = "3857"
                else:
                    prj = "4326"

                # TODO: switch between processes
                if prj == "3857":
                    output_file_name = filename + ".geotiff"
                    print "Processing:", output_file_name
                    # TODO: worksaround for the various sourcepath e dstpath
                    process_obj_3857[0]["source_path"] = [f]
                    process_obj_3857[0]["output_path"] = output_path
                    process_obj_3857[0]["output_file_name"] = output_file_name
                    for p in process_obj_3857:
                        p["source_path"] = p["source_path"] if "source_path" in p else result
                        result = process_obj(p)
                elif prj == "4326":
                    output_file_name = filename + "_" + prj + ".geotiff"
                    print "Processing:", output_file_name
                    process_obj_4326[0]["source_path"] = [f]
                    process_obj_4326[0]["output_path"] = output_path
                    process_obj_4326[0]["output_file_name"] = output_file_name
                    for p in process_obj_4326:
                        p["source_path"] = p["source_path"] if "source_path" in p else result
                        result = process_obj(p)


def create_output_folder(folder):
    # if os.path.exists(folder):
    #     shutil.rmtree(folder)

    if not os.path.exists(folder):
        os.makedirs(folder)

    return folder


def process_burned_areas_foolders(src_folder, dest_folder, file_type):
    folders = glob.glob(os.path.join(src_folder, "*"))
    for folder in folders:
        if os.path.isdir(folder):
            print folder
            dest = os.path.join(folder, dest_folder)
            process(folder, dest, file_type)


def rename_folders(src_folder):
    folders = glob.glob(os.path.join(src_folder, "*"))
    for folder in folders:
        if os.path.isdir(folder):
            os.rename(folder, folder.replace(" ", "_"))


def rename_burned_areas_output_files(src_folder, dest_folder, file_type="geotiff"):
    folders = glob.glob(os.path.join(src_folder, "*"))
    for folder in folders:
        if os.path.isdir(folder):
            output_folder = os.path.join(folder, dest_folder)
            files = glob.glob(os.path.join(output_folder, "*." + file_type))
            for f in files:
                print f
                filename = get_filename(f)
                renamed_filename = burned_areas_switch(filename).replace(" ", "_")
                prj = filename.split("_")[len(filename.split("_"))-1]
                year = filename.split("_")[len(filename.split("_"))-2]
                renamed_filename += "_" + year + "_" + prj + "." + file_type
                os.rename(f, os.path.join(output_folder, renamed_filename))


def burned_areas_switch(filename):
    filename = filename.lower()
    if "peatlands" in filename:
        return "Burned_Areas_-_Organic_soils"
    if "AllForestsMinus".lower() in filename:
        return "Burned_Areas_-_Other forest"
    if "humidtropicalforests".lower() in filename:
        return "Burned Areas_-_Humid Tropical Forest"

    burned_areas_lc = "Burned Areas_-_"
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



# load scripts
if __name__ == '__main__':
    src_folder  = "/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/Theory_structure_novemeber_13/GFED4_BURNEDAREAS_BY_LANDCOVER/"
    dest_folder = "output"

    #rename_folders(src_folder)
    #process_burned_areas_foolders(src_folder, dest_folder, "tif")
    #process_burned_areas_foolders(src_folder, dest_folder, "tiff")

    #rename output files
    #rename_burned_areas_output_files(src_folder, dest_folder)


    #process(src_folder, dest_folder, "geoserver", "3857")
    #process(src_folder, dest_folder, "storage", "4326")

    #move_storage_folder(os.path.join(dest_folder, "earthstat_crop_area/storage/"))
    #move_storage_folder(os.path.join(dest_folder, "earthstat_crop_yield/storage/"))

    # N.B. the final move has been made by hand
    # earthstat/earthstat_processeddata/
    # earthstat/earthstat_processeddata/geoserver/
    # earthstat/earthstat_processeddata/geoserver/earthstat_crop_area/
    # earthstat/earthstat_processeddata/geoserver/earthstat_crop_yield/
    # earthstat/earthstat_processeddata/storage/earthstat_crop_area/
    # earthstat/earthstat_processeddata/storage/earthstat_crop_area/abacaarea_4326/
    # etc...