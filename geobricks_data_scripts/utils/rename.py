import os
import glob
from geobricks_common.core.filesystem import get_filename

def rename_files(src_folder, from_file_type="tif", to_file_type="geotiff"):
    folders = glob.glob(os.path.join(src_folder, "*"))
    for folder in folders:
        if os.path.isdir(folder):
            files = glob.glob(os.path.join(folder, "*." + from_file_type))
            for f in files:
                filename = get_filename(f)
                output_path = os.path.join(folder, filename + "." + to_file_type)
                os.rename(f, output_path)


# rename_files("/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/MAGHG-data/OUTPUT/geoserver/")