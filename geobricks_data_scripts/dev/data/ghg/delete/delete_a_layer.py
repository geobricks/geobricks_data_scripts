
from geobricks_data_scripts.dev.utils.data_manager_util import get_data_manager

data_manager = get_data_manager()

data_manager.delete("ghg:dm_burning_savanna_2002_3857")
data_manager.delete("ghg:ch4_emissions_burning_otherforests_2004_3857")
