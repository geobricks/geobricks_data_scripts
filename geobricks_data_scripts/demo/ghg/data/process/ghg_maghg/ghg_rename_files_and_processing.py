import os
import glob
import ntpath
import shutil
from geobricks_processing.core.processing_core import process_data



process_obj_emission_factor = [
    {
        # "output_path": output_path + "/gdal_translate",
        # "output_file_name": "MOD13A2_3857.tif",
        "process": [
            {
                "gdal_translate": {
                    "opt": {
                        "-co": "'TILED=YES'",
                        "-co": "'COMPRESS=DEFLATE'"
                        # ,"-a_nodata": 0
                    }
                }
            }
        ]
    },
    {
        "process": [
            {
                "gdaladdo": {
                    "parameters": {},
                    "overviews_levels": "2 4 8 16"
                }
            }
        ]
    }
]

process_obj_burned_areas = [
    {
        # "output_path": output_path + "/gdal_translate",
        # "output_file_name": "MOD13A2_3857.tif",
        "process": [
            {
                "gdal_translate": {
                    "opt": {
                        "-co": "'TILED=YES'",
                        "-co": "'COMPRESS=DEFLATE'",
                        "-a_nodata": 0
                    }
                }
            }
        ]
    },
    {
        "process": [
            {
                "gdaladdo": {
                    "parameters": {},
                    "overviews_levels": "2 4 8 16"
                }
            }
        ]
    }
]


def process():
    files = glob.glob("/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/MAGHG-data/*.tif")
    output_path = "/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/MAGHG-data/OUTPUT/"
    if os.path.isdir(output_path):
        shutil.rmtree(output_path)
        os.mkdir(output_path)
    for f in files:
        folder, filename = os.path.split(f)
        if "_EF_" in filename:
            process_obj = process_obj_emission_factor
        else:
            process_obj = process_obj_burned_areas

        process_obj[0]["source_path"] = [f]
        process_obj[0]["output_path"] = output_path
        process_obj[0]["output_file_name"] = filename
        process_data(process_obj)


def rename_files():
    files = glob.glob("/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/MAGHG-data/*.tif")
    for f in files:
        if "_GFED4BA_" in f:
            renamed_file = f.replace("_GFED4BA_", "_")
            os.rename(f, renamed_file)
        if "_GFED4_" in f:
            renamed_file = f.replace("_GFED4_", "_")
            print f, renamed_file
            os.rename(f, renamed_file)


def lyr_filenames():
    files = glob.glob("/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/MAGHG-data/*.lyr")
    for f in files:
        folder, filename = os.path.split(f)
        print filename


def rename_lyr_filenames():
    files = glob.glob("/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/MAGHG-data/*.lyr")
    for f in files:
        folder, filename = os.path.split(f)
        renamed_file = f.replace(".tif", "")
        renamed_file = f.replace("_4326", "")
        os.rename(f, renamed_file)


rename_lyr_filenames()
lyr_filenames()



