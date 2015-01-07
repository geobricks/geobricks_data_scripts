from geobricks_data_scripts.dev.utils.data_manager_util import get_data_manager
data_manager = get_data_manager()


# TODO How to handle the fact that is in storage?
data_manager.delete("mod13a2", True, False, False)
