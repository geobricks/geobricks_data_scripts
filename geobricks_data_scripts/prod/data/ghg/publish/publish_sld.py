from geobricks_geoserver_manager.config.config import config
from geobricks_geoserver_manager.core.geoserver_manager_core import GeoserverManager
from geobricks_common.core.filesystem import get_filename
import glob


def import_slds():
    geoserver_manager = GeoserverManager(config)
    for path in glob.glob("/home/vortex/Desktop/LAYERS/ghg/geodata_handedoverto_simonem/*.sld"):
        with open(path, 'r') as f:
            data = f.read()
            filename = get_filename(path).lower()
            geoserver_manager.publish_style(filename + "_EN", data)


#import_slds()
