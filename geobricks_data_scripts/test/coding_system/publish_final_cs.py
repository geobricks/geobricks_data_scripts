import csv
import json

from geobricks_metadata_manager.core.metadata_manager_d3s_core import MetadataManager
from geobricks_data_scripts.demo.config.config import settings

metadata_manager = MetadataManager(settings)

print metadata_manager

cs = {
    "metadata": {
        "uid": "layer_products",
        "version": "1.0",
        "title": {
            "EN": "Layers"
        },
        "meContent": {
            "resourceRepresentationType": "codelist"
        }
    },
    "data": [

    ]
}


with open('csv/final.csv', 'rb') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        cs["data"].append({
            "code": row[0],
            "title": {
                "EN": row[1]
            }
        })


print json.dumps(cs)
print metadata_manager.publish_coding_system(cs, True)



