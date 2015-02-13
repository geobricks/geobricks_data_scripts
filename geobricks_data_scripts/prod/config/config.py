import logging
import os
import json

settings = {

    "settings": {


        # To be used by Flask: DEVELOPMENT ONLY
        "debug": True,

        # Flask host: DEVELOPMENT ONLY
        "host": "localhost",

        # Flask port: DEVELOPMENT ONLY
        "port": 5555,

        # Logging configurations
        "logging": {
            "level": logging.ERROR,
            "format": "%(asctime)s | %(levelname)-8s | %(name)-20s | Line: %(lineno)-5d | %(message)s",
            "datefmt": "%d-%m-%Y | %H:%M:%s"
        },

        # Email configurations
        "email": {
            "settings": "path_to_the_email.json",
            "user":  None,
            "password": None
        },

        # Folders
        "folders": {
            "config": "config/",
            "tmp": "/home/vortex/Desktop/LAYERS/geobricks/tmp/",
            "geoserver_datadir": "/home/vortex/programs/SERVERS/tomcat_geoservers/geoserver_data_2_5_3/data/",
            "distribution": "/home/vortex/Desktop/LAYERS/geobricks/distribution/",
            "storage": "/home/vortex/Desktop/LAYERS/geobricks/storage/"
        },

        # Geoserver
        "geoserver": {
            "geoserver_master": "http://fenix.fao.org:20200/geoserver/rest",
            "geoserver_slaves": [],
            "username": "fenix",
            "password": "Fenix2014",
        },

        # Metadata
        "metadata": {
            "url_create_metadata": "http://fenix.fao.org/d3s/msd/resources/metadata",
            "url_get_metadata_uid": "http://fenix.fao.org/d3s/msd/resources/metadata/uid/<uid>",

            # delete metadata
            "url_delete_metadata": "http://fenix.fao.org/d3s/msd/resources/metadata/uid/<uid>",

            # get metadata
            "url_get_metadata": "http://fenix.fao.org/d3s/msd/resources/find",
            "url_get_metadata_full": "http://fenix.fao.org/d3s/msd/resources/metadata/uid/<uid>?full=true&dsd=true",

            # coding system
            "url_create_coding_system": "http://fenix.fao.org/d3s/msd/resources",
            "url_data_coding_system": "http://fenix.fao.org/d3s/msd/resources/data/uid/<uid>",

            # DSD
            "url_overwrite_dsd_rid": "http://fenix.fao.org/d3s/msd/resources/dsd"
        }
    }
}


# Setting email adderess from configuration file
def set_email_settings():
    if os.path.isfile(settings["settings"]["email"]["settings"]):
        settings["settings"]["email"] = json.loads(open(settings["settings"]["email"]["settings"]).read())
set_email_settings()