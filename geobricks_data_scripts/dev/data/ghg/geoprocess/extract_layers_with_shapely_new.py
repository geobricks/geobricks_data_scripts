

# working
import fiona
from shapely.geometry import shape

input_gaul = '/home/vortex/Desktop/LAYERS/GAUL/simone/gaul0_2008.shp'
input_shp = '/home/vortex/Desktop/LAYERS/ghg/process_data/3857/CH4_Emissions_Burning_ClosedShrublands/CH4_GFED4BA_Emissions_Burning_ClosedShrublands_1997_3857.shp'
filapath = '/home/vortex/Desktop/LAYERS/GAUL/simone/ita.shp'

with fiona.open(input_gaul) as gaul:
    # geom_gaul = []
    # for g in gaul:
    #     geom_gaul.append(shape(g['geometry']))
    # print 'finished geometry'

    with fiona.open(input_shp) as shp:
        sink_schema = shp.schema.copy()
        with fiona.open(
                filapath, 'w',
                crs=shp.crs,
                driver=shp.driver,
                schema=sink_schema,
        ) as sink:
            print 'here'
            for s in shp:
                geom_shp = shape(s['geometry'])

            print "end"
                # for g in geom_gaul:
                #     if geom_shp.intersection(g):
                #         sink.write(s)
                #         print "daje"





