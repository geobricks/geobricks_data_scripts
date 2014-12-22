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
            "tmp": "tmp_path",
            "geoserver_datadir": "/home/vortex/programs/SERVERS/tomcat_geoservers/geoservers-test/data/",
            "distribution": "distribution_folder",
            "ftp": "ftp_folder"
        },

        # Geoserver
        "geoserver": {
            "geoserver_master": "http://lprapp16.fao.org:20100/geoserver/rest",
            "geoserver_slaves": [],
            "username": "fenix",
            "password": "Fenix2014",
            },

        # Metadata
        "metadata": {
            "url_create_metadata": "http://fenix.fao.org/d3s_dev/msd/resources/metadata",
            "url_get_metadata_uid": "http://fenix.fao.org/d3s_dev/msd/resources/metadata/uid/<uid>",
            "url_get_metadata": "http://fenix.fao.org/d3s_dev/msd/resources/find",
            "url_create_coding_system": "http://fenix.fao.org/d3s_dev/msd/resources"
        }
    }
}


# Setting email adderess from configuration file
def set_email_settings():
    if os.path.isfile(settings["settings"]["email"]["settings"]):
        settings["settings"]["email"] = json.loads(open(settings["settings"]["email"]["settings"]).read())
set_email_settings()