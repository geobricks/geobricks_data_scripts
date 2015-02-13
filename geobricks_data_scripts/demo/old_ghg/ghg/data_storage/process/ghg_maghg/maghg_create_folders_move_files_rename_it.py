import os
import glob
from geobricks_common.core.filesystem import get_filename
import ntpath
import shutil

# N.B. we assume that the files are already been processed

# create foldes, move files and rename it in case
def process_files():
    files = glob.glob("/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/MAGHG-data/OUTPUT/*.tif")
    output_path = "/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/MAGHG-data/OUTPUT/storage"
    if not os.path.isdir(output_path):
        # shutil.rmtree(output_path)
        os.mkdir(output_path)

    # for each file
    for f in files:
        # get filename
        filename = get_filename(f)
        extension = f.split(".")[1]

        # if _4326 projection
        if filename.endswith("_4326"):
            # create the folder
            folder_to_move_path = create_folder(output_path, filename)

            # move the file to the returned folder path
            final_path = os.path.join(folder_to_move_path, filename + "." + extension)
            print "Final path: " + str(final_path)
            shutil.move(f, final_path)

            # rename the file is it's not yet .geotiff
            if not final_path.endswith(".geotiff"):
                 f_geotiff = final_path.replace("."+extension, ".geotiff")
                 print "Renaming to: " + str(f_geotiff)
                 os.rename(final_path, f_geotiff)


def create_folder(path, filename):
    path = os.path.join(path, filename)
    if not os.path.isdir(path):
        os.mkdir(path)
    return path





def move_to_another_folder(src_folder, file_type="geotiff"):
    folders = glob.glob(os.path.join(src_folder, "*"))
    for folder in folders:
        if os.path.isdir(folder):
            files = glob.glob(os.path.join(folder, "*." + file_type))
            for f in files:
                print f, src_folder
                filename = get_filename(f)
                output_path = os.path.join(src_folder, filename+ "." + file_type)
                shutil.copyfile(f, output_path)


#process_files()
move_to_another_folder("/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/MAGHG-data/OUTPUT/storage/")