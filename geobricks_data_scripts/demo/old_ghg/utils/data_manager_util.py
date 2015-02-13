from geobricks_data_manager.core.data_manager_core import DataManager
from geobricks_data_scripts.demo.old_ghg.config.config import settings

 # get the default data manager for demo db
def get_data_manager():
    return DataManager(settings)