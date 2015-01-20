from geobricks_common.core.log import logger
from geobricks_data_scripts.dev.utils.data_manager_util import get_data_manager

log = logger(__file__)

data_manager = get_data_manager()

try:
    # TODO How to handle the fact that is in storage?
    data_manager.delete("ghg:cultivation_organic_soils_-_croplands_3857", True, False, False)
    data_manager.delete("cultivation_organic_soils_-_croplands_4326", True, False, False)

    data_manager.delete("ghg:sheep10km_ad_2010_v2_2010_3857", True, False, False)
    data_manager.delete("sheep10km_ad_2010_v2_2010_4326", True, False, False)
    data_manager.delete("ghg:cattle10km_ad_2010_v2_2010_3857", True, False, False)
    data_manager.delete("cattle10km_ad_2010_v2_2010_4326", True, False, False)
except Exception, e:
    log.error(e)
    pass
