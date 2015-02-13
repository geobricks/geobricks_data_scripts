import os
import glob
from geobricks_common.core.log import logger
from geobricks_data_scripts.prod.utils.data_manager_util import get_data_manager
from geobricks_data_scripts.utils.harvest.publish_harvest import harvest_folder

log = logger(__file__)

data_manager = get_data_manager()

data_manager.check_consistency()
