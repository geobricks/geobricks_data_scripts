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
        #"output_file_name": "burundi_maize_area_4326.tif",
        "band": 1,
        "tmp": True,
        "process": [
            {
                "gdalwarp": {
                    "opt": {
                        "-multi": "",
                        "-overwrite": "",
                        "-of": "GTiff",
                        "-srcnodata": "8.999999828524175e+20",
                        "-dstnodata": "-3000",
                        "-s_srs": "EPSG:4326",
                        "-t_srs": "EPSG:3857"
                    }
                }
            }
        ]
    },
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
                        "-a_nodata": "-3000",
                        "-a_srs": "EPSG:3857",
                        "-co": "'TILED=YES'",
                        "-co": "'COMPRESS=DEFLATE'",
                    }
                }
            },
            {
                "gdaladdo": {
                    "parameters": {
                        # "--config": "BIGTIFF_OVERVIEW IF_NEEDED"
                    },
                    "overviews_levels": "2 4 8 16"
                }
            }
        ]
    },
    # {
    #     "band": 1,
    #     "process": [
    #         {
    #             "gdaladdo": {
    #                 "parameters": {
    #                     # "--config": "BIGTIFF_OVERVIEW IF_NEEDED"
    #                 },
    #                 "overviews_levels": "2 4 8 16"
    #             }
    #         }
    #     ]
    # }
]


process_obj_4326 = [
    {
        "band": 1,
        "process": [
            {
                "gdalwarp": {
                    "opt": {
                        "-multi": "",
                        "-overwrite": "",
                        "-of": "GTiff",
                        "-srcnodata": "8.999999828524175e+20",
                        "-dstnodata": "-3000",
                        "-s_srs": "EPSG:4326",
                        "-t_srs": "EPSG:4326"
                    }
                }
            }
        ]
    },
    {
        "band": 1,
        "process": [
            {
                "gdal_translate": {
                    "opt": {
                        "-of": "GTiff",
                        "-a_nodata": "-3000",
                        "-a_srs": "EPSG:4326",
                        "-co": "'COMPRESS=DEFLATE'",
                        }
                }
            }
        ]
    },
]

def process(src_folder, dest_folder="", folder_type="geoserver", prj="3857", overwrite=True, file_type="tif"):
    folders = glob.glob(os.path.join(src_folder, "*"))
    for folder in folders:
        if os.path.isdir(folder):
            # dest_folder = create_output_folder(folder, folder_type, overwrite)
            files = glob.glob(os.path.join(folder, "*." + file_type))
            for f in files:
                if "area" in f:
                    output_path = os.path.join(dest_folder, "earthstat_crop_area")
                elif "yield" in f:
                    output_path = os.path.join(dest_folder, "earthstat_crop_yield")

                output_path = create_output_folder(output_path, folder_type, overwrite)

                filename = get_filename(f)
                if filename[len(filename)-1] == "1":
                    filename = filename[:-1]
                output_file_name = filename + "_" + prj + ".geotiff"
                # TODO: switch between processes
                print "Processing:", output_file_name
                if prj == "3857":
                    # TODO: worksaround for the various sourcepath e dstpath
                    process_obj_3857[0]["source_path"] = [f]
                    process_obj_3857[1]["output_path"] = output_path
                    process_obj_3857[1]["output_file_name"] = output_file_name
                    for p in process_obj_3857:
                        p["source_path"] = p["source_path"] if "source_path" in p else result
                        result = process_obj(p)
                elif prj == "4326":
                    process_obj_4326[0]["source_path"] = [f]
                    process_obj_4326[1]["output_path"] = output_path
                    process_obj_4326[1]["output_file_name"] = output_file_name
                    for p in process_obj_4326:
                        p["source_path"] = p["source_path"] if "source_path" in p else result
                        result = process_obj(p)


def create_output_folder(folder, folder_type="geoserver", overwrite=False):
    dest_folder = os.path.join(folder, folder_type)
    # if folder exists remove it and create if again
    # if overwrite:
    #     if os.path.exists(dest_folder):
    #         shutil.rmtree(dest_folder)
    # if not os.path.exists(dest_folder):
    #     os.makedirs(dest_folder)
    return dest_folder


def move_storage_folder(base_folder, file_type="geotiff"):
    files = glob.glob(os.path.join(base_folder, "*." + file_type))

    for f in files:
        print f
        if os.path.isfile(f):
            print f
            filename = get_filename(f)
            folder = os.path.join(base_folder, filename)
            if not os.path.isdir(folder):
                os.makedirs(folder)
            print folder
            # move file to folder
            shutil.move(f, folder)




# load scripts
if __name__ == '__main__':
    src_folder  = "/home/vortex/Desktop/LAYERS/earthstat/175CropsYieldArea_geotiff/"
    dest_folder = "/home/vortex/Desktop/LAYERS/earthstat/earthstat_processeddata/"


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