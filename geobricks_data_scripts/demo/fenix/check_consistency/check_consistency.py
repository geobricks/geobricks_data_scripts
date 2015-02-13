from geobricks_common.core.log import logger
from geobricks_data_scripts.demo.fenix.utils.data_manager_util import get_data_manager

log = logger(__file__)

data_manager = get_data_manager()

result = data_manager.check_consistency()

for r in result["storage"]:
    log.info(r)

for r in result["geoserver"]:
    log.info(r)