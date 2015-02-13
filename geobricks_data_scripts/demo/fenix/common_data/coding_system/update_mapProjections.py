from geobricks_data_scripts.demo.fenix.utils.data_manager_util import get_data_manager

data_manager = get_data_manager()

cs = {
    "metadata": {
        "uid": "mapProjections",
        "version": "1.0"
    },
    "data": [
        {
            "code": "EPSG:4326",
            "title": {
                "EN": "Latlong"
            }
        },
        {
            "code": "EPSG:3857",
            "title": {
                "EN": "Spherical Mercator projection"
            }
        },
        {
            "code": "EPSG:900913",
            "title": {
                "EN": "Equivalent to Spherical Mercator Projection"
            }
        }
    ]
}

# Update coding system
data_manager.metadata_manager.update_coding_system(cs, True)