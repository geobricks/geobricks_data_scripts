from osgeo import ogr
from shapely.wkb import loads
from shapely.geometry import *
import fiona

#first layer, a polygon shapefile
# first = Polygon()
# # open shapefile
# source1 = ogr.Open("/home/vortex/Desktop/LAYERS/GAUL/GAUL0_FAOSTAT_3857_PROSPERI/countries/1.shp")
# layer1 = source1.GetLayer()
#
# print "1"
# # combination of all the geometries of the layer in a single shapely object
# for element in layer1:
#     geom = loads(element.GetGeometryRef().ExportToWkb())
#     first = first.union(geom)
#     # second layer, a polygon shapefile
#
# print "2"
# two = Polygon()
# source2 = ogr.Open("/home/vortex/Desktop/LAYERS/ghg/process_data/3857/FuelBiomass/Burning_WoodySavanna_FuelBiomass_3857.shp")
# layer2 = source2.GetLayer()
# for element in layer2:
#     geom = loads(element.GetGeometryRef().ExportToWkb())
#     two = two.union(geom)
#
# print "3"
# shp = fiona.open("/home/vortex/Desktop/LAYERS/ghg/process_data/3857/FuelBiomass/Burning_WoodySavanna_FuelBiomass_3857.shp")
# sink_schema = shp.schema.copy()
# print sink_schema
# # intersection between the two layers
# output = fiona.open('/home/vortex/Desktop/LAYERS/ghg/process_data/test/test.hsp', 'w', crs=shp.crs, driver=shp.driver, schema=sink_schema)
# output.write(first.intersection(two))

shp = fiona.open("/home/vortex/Desktop/LAYERS/ghg/process_data/3857/FuelBiomass/Burning_WoodySavanna_FuelBiomass_3857.shp")
for feat in shp:
    print feat