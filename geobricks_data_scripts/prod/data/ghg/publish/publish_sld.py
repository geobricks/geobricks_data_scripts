from geobricks_data_scripts.prod.utils.data_manager_util import get_data_manager
from geobricks_common.core.filesystem import get_filename
import glob


def import_slds():
    data_manager = get_data_manager()
    for path in glob.glob("/home/vortex/repos/FENIX-MAPS/geobricks/geobricks_data_scripts/geobricks_data_scripts/geoserver_sld/*.sld"):
        with open(path, 'r') as f:
            data = f.read()
            stylename = get_filename(path).lower()
            # if stylename[-3:] == "_en":
            #     stylename = stylename[:len(stylename)-3] + "_EN"
            overwrite = False
            print "Uploading Style: %s (overwrite %s) " % (stylename, overwrite)

            data_manager.geoserver_manager.publish_style(stylename, data, overwrite)
            #data_manager.geoserver_manager.delete_style(stylename)


import_slds()
