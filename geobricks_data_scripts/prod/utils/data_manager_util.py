from geobricks_data_manager.core.data_manager_core import DataManager
from geobricks_data_scripts.prod.config.config import settings

 # get the default data manager for demo db
def get_data_manager():
    print "Prod DAata Manager"
    print settings
    return DataManager(settings)