import glob
import fiona
import pprint
import os
import shutil
from geobricks_common.core.filesystem import get_filename

# extract all gaul countries
def extract_gaul_shp(input_path, output_path):
    output_folder = os.path.join(output_path)
    if os.path.isdir(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder)

    with fiona.open(input_path) as source:
        print source.crs
        sink_schema = source.schema.copy()

        for f in source:
            #print f['properties']
            # print f['properties'].get('ADM0_CODE')
            # print f['properties'].get('ADM0_NAME')
            if f['properties'].get('DISP_AREA') is not 'NO':
                print f['properties'].get('ADM0_CODE'), f['properties'].get('ADM0_NAME')
                filapath = os.path.join(output_path, str(int(f['properties'].get('ADM0_CODE'))) + ".shp")
                print filapath
                with fiona.open(
                        filapath, 'w',
                        crs=source.crs,
                        driver=source.driver,
                        schema=sink_schema,
                ) as sink:
                    sink.write(f)

        #print s
    #print len(list(shp))

#extract_gaul_shp('/home/vortex/Desktop/LAYERS/GAUL/GAUL_2014/4326/g2014_2013_0/G2014_2013_0.shp', '/home/vortex/Desktop/LAYERS/GAUL/GAUL_2014/4326/g2014_2013_0/countries')

input_gaul_folder = '/home/vortex/Desktop/LAYERS/GAUL/GAUL0_FAOSTAT_3857_PROSPERI/GAUL_FAOSTAT_3857_PROSPERI.shp'
output_gaul_folder = '/home/vortex/Desktop/LAYERS/GAUL/GAUL0_FAOSTAT_3857_PROSPERI/countries/'
extract_gaul_shp(input_gaul_folder, output_gaul_folder)