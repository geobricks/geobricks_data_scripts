import os
import glob
import shutil
from geobricks_common.core.filesystem import get_filename



# Raster Data
def preprocess_raster_data_for_storage(srs_folder, dst_folder, filetype="tif"):
    folders = glob.glob(srs_folder +"/*")
    for folder in folders:
        if os.path.isdir(folder):
            files = glob.glob(folder + "/*." + filetype)
            for src_file in files:
                _move_raster_file_to_storage(dst_folder, src_file)

# Move the raster to the storage folders
def _move_raster_file_to_storage(dst_folder, src_file, output_filetype="geotiff"):

    src_filename = get_filename(src_file.lower())
    # lowercase (everything is lowercase)

    dst_folder_file = os.path.join(dst_folder, get_filename(src_filename))

    # create folder
    if os.path.isdir(dst_folder_file) is True:
        shutil.rmtree(dst_folder_file)
    os.mkdir(dst_folder_file)

    # move file
    dst_file_path = os.path.join(dst_folder_file, src_filename + "." + output_filetype)
    shutil.copy(src_file, dst_file_path)



# Move the raster to the storage folders
def crop_raster_layers_by_gaul0():
    print "TODO: crop_raster_layers_by_gaul0"


# Vector Data
def preprocess_vector_data_for_storage(srs_folder, dst_folder, filetype="shp"):
    folders = glob.glob(srs_folder +"/*")
    for folder in folders:
        if os.path.isdir(folder):
            files = glob.glob(folder + "/*." + filetype)
            for src_file in files:
                path, filename_ext, filename = get_filename(src_file, True)
                print path, filename_ext, filename
                # get all shapefile reference files
                shpfiles = glob.glob(path + "/" + filename + ".*")
                _move_vector_files_to_storage(dst_folder, filename.lower(), shpfiles)

def _move_vector_files_to_storage(dst_folder, dst_filename, src_files):
    print "_move_vector_files_to_storage"

    dst_folder_file = os.path.join(dst_folder, dst_filename)
    print dst_folder_file

    # create folder
    if os.path.isdir(dst_folder_file) is True:
        shutil.rmtree(dst_folder_file)
    os.mkdir(dst_folder_file)

    # move files
    for src_file in src_files:
        path, filename_ext, filename = get_filename(src_file, True)
        dst_file_path = os.path.join(dst_folder_file, filename_ext)
        print dst_file_path
        shutil.copy(src_file, dst_file_path)



if __name__ == '__main__':
    # Folders
    storage_raster_folder = "/home/vortex/Desktop/LAYERS/ghg/process_data/storage/raster"
    storage_vector_folder = "/home/vortex/Desktop/LAYERS/ghg/process_data/storage/vector"
    process_data_folder = "/home/vortex/Desktop/LAYERS/ghg/process_data"

    # 4326 Raster Data
    # preprocess_raster_data_for_storage(process_data_folder + "/4326", storage_raster_folder)

    # 3975 Raster Data
    #preprocess_vector_data_for_storage(process_data_folder + "/3975", storage_vector_folder)

    # 3975 Raster Data
    #preprocess_vector_data_for_storage(process_data_folder + "/3975", storage_vector_folder)