from geobricks_data_manager.core.data_manager_core import DataManager
from geobricks_data_scripts.prod.ghg.config.config import settings

 # get the default data manager for demo db
def get_data_manager():
    print "Prod Data Manager"
    print settings
    return DataManager(settings)