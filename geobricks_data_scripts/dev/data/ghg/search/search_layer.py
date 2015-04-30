from geobricks_data_scripts.dev.utils.data_manager_util import get_data_manager
import os

data_manager = get_data_manager()

#layers = data_manager.metadata_manager.get_by_layername_workspace("gfed4_burnedarea_mixedforest_2002_3857", "ghg")

layers = data_manager.metadata_manager.get_all_layers()

count_4326 = 0
count_3857 = 0

for l in layers:
    print l["meReferenceSystem"]["seProjection"]["projection"]["codes"]
    if "4326"in l["meReferenceSystem"]["seProjection"]["projection"]["codes"][0]["code"]:
        count_4326 += 1
    elif "3857"in l["meReferenceSystem"]["seProjection"]["projection"]["codes"][0]["code"]:
        count_3857 += 1
    else:
        print "NOOO"

print count_4326
print count_3857


#print os.path.isfile("/home/vortex/Desktop/LAYERS/ghg/geodata_handedoverto_simonem/4326/CH4_Emissions_Burning_HumidTropicalForests/CH4_GFED4BA_Emissions_Burning_HumidTropicalForests_1997_4326.tif")

