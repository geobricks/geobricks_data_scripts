import fiona
from shapely.geometry import shape
import rtree

def create_gaul_layers(filepath1, filepath2):
    with fiona.open(filepath1, 'r') as layer1:
        with fiona.open(filepath2, 'r') as layer2:
            print "Preparing GAUL0 Indexes"
            features = {}
            index = rtree.index.Index()
            for feat1 in layer1:
                fid = int(feat1['id'])
                gaul_code = feat1['properties'].get('ADM0_CODE')
                geom1 = shape(feat1['geometry'])
                index.insert(fid, geom1.bounds)
                features[fid] = (feat1, geom1, gaul_code)

            print "Start searching features"
            for feat2 in layer2:
                geom2 = shape(feat2['geometry'])
                print "-------"
                for fid in list(index.intersection(geom2.bounds)):
                    if fid != int(feat2['id']):
                        # check geometry intersection
                        feat1, geom1, gaul_code = features[fid]
                        print gaul_code
            print "End"

filepath1 = '/home/vortex/Desktop/LAYERS/GAUL/simone/gaul0_2008.shp'
filepath2 = '/home/vortex/Desktop/LAYERS/ghg/process_data/3857/CH4_Emissions_Burning_ClosedShrublands/CH4_GFED4BA_Emissions_Burning_ClosedShrublands_1998_3857.shp'


create_gaul_layers(filepath1, filepath2)
