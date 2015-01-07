from geobricks_data_scripts.demo.utils.data_manager_util import get_data_manager
data_manager = get_data_manager()


# TODO How to handle the fact that is in storage?
data_manager.delete_coveragestore("mod13a2")
