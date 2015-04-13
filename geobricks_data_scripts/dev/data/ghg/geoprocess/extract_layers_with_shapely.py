

# working
import fiona
from shapely.geometry import shape

input_gaul = '/home/vortex/Desktop/LAYERS/GAUL/simone/gaul0_2008.shp'
input_shp = '/home/vortex/Desktop/LAYERS/ghg/process_data/3857/CH4_Emissions_Burning_ClosedShrublands/CH4_GFED4BA_Emissions_Burning_ClosedShrublands_1997_3857.shp'
filapath = '/home/vortex/Desktop/LAYERS/GAUL/simone/ita.shp'

with fiona.open(input_gaul) as gaul:
    with fiona.open(input_shp) as shp:
        sink_schema = shp.schema.copy()
        with fiona.open(
                    filapath, 'w',
                    crs=shp.crs,
                    driver=shp.driver,
                    schema=sink_schema,
            ) as sink:
            for g in gaul:
                if g['properties'].get('ADM0_NAME') == 'Italy':
                    print g['properties'].get('ADM0_CODE'), g['properties'].get('ADM0_NAME')
                    geom_gaul = shape(g['geometry'])
                    for s in shp:
                        #print s['properties']
                        geom_shp = shape(s['geometry'])
                        if geom_gaul.intersection(geom_shp):
                            sink.write(s)
                            print "daje"
                    break

