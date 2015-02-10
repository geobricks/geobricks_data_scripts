import os
import glob
import shutil
from geobricks_common.core.filesystem import get_filename

# Copy files used for Storage (4326 Layers) to be compliant with the storage_structure
def copy_files(src_folder, file_type="geotiff"):
    folders = glob.glob(os.path.join(src_folder, "*"))
    for folder in folders:
        if os.path.isdir(folder):
            # print folder
            files = glob.glob(os.path.join(folder, "*." + file_type))
            for f in files:
                filename = get_filename(f)
                dst_file = os.path.join(src_folder, filename + "." + file_type)
                print f
                print dst_file
                shutil.copyfile(f, dst_file)




# copy_files("/home/vortex/Desktop/LAYERS/earthstat/earthstat_processeddata/storage/earthstat_crop_area/")
# copy_files("/home/vortex/Desktop/LAYERS/earthstat/earthstat_processeddata/storage/earthstat_crop_yield/")