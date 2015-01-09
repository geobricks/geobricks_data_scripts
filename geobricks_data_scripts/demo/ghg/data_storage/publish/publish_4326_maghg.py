import os
import glob
from geobricks_common.core.filesystem import sanitize_name, get_filename
from geobricks_data_scripts.demo.utils.data_manager_util import get_data_manager

data_manager = get_data_manager()

# WORKSPACE TO USED DURING THE UPDATE
WORKSPACE = "ghg"

#STORAGE FOLDER
STORAGE_FOLDER = "/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/MAGHG-data/OUTPUT/storage/"



# create foldes, move files and rename it in case
def process_metadata(workspace, storage_folder):
    folders = glob.glob(storage_folder+ "*")

    # for each file
    for f in folders:
        print "-------------"
        print "folder: " + f

        # get filename (it's the same as the folder)
        filename = get_filename(f)
        print "filename: " + f

        # get UID of the file
        uid = sanitize_name(filename)
        print "uid stored layer: " + uid

        # get UID of the stored 3857 projection file
        uid_3857 = sanitize_name(workspace + ":" + filename.rsplit("_", 1)[0])
        print "uid_3857 to search: " + uid_3857

        # get path to the file (+.geotiff extention)
        path_file = os.path.join(f, filename + ".geotiff")

        print "path_file: " + path_file
        update_published_layer_with_distribution_uid(uid_3857, uid)


def update_published_layer_with_distribution_uid(uid_3857, uid):
    print "-> update_published_layer_with_distribution_uid\n   [%s, %s]" % (uid_3857, uid)

    # search the metadata uid_3857
    try:
        metadata_3857 = data_manager.metadata_manager.get_by_uid(uid_3857)

        print metadata_3857["uid"], metadata_3857["dsd"]

        # update dsd rid with distribution uid
    except Exception,e:
        print e

process_metadata(WORKSPACE, STORAGE_FOLDER)