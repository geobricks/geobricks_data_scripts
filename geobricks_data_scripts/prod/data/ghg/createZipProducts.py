import glob
import os
import shutil
from geobricks_common.core.filesystem import createZip


def createGHGProducts(obj):
    inputPath = obj["inputPath"]
    outputPath = obj["outputPath"]
    archiveType = obj["archiveType"]
    codingSystem = obj["codingSystem"] if "codingSystem" in obj else None
    zips = obj["zippit"]

    # Get all country codes (to be used in the folder input and output folder construction
    # TODO: how to make generic?
    codes_folders = glob.glob(os.path.join(inputPath, "*"))
    codes = []
    for folder in codes_folders:
        codes.append(os.path.split(folder)[1])

    # create the zip files
    for to_zip in zips:
        print to_zip["name"]
        outputFilename = to_zip["filename"]
        outputFolderName = to_zip["folderName"]

        # for each country code
        for code in codes:

            # TODO: get all country codes (to be used in the folder input construction)

            # TODO add to the path gaul code i.e. 4326/product/faostat/12/product_name.zip
            # Create Product
            outputFolderPath = os.path.join(outputPath, outputFolderName)
            if not os.path.isdir(outputFolderPath):
                os.makedirs(outputFolderPath)

            # Create Coding System
            if codingSystem:
                outputFolderPath = os.path.join(outputFolderPath, codingSystem)
                if not os.path.isdir(outputFolderPath):
                    os.makedirs(outputFolderPath)

            # Create output folder and subfolder
            outputFolderPath = os.path.join(outputFolderPath, code)
            if not os.path.isdir(outputFolderPath):
                os.makedirs(outputFolderPath)

            outputFilePath = os.path.join(outputFolderPath, outputFilename)

            # delete file if already exists
            if os.path.isfile(outputFilePath):
                os.remove(outputFilePath)

            folders_to_zip = []
            for folder in to_zip["folders"]:
                # TODO add to the path gaul code i.e. inputPath/12/inputFolder
                folders_to_zip.append(os.path.join(inputPath, code, folder))

            # create zip file
            createZip(outputFilePath, folders_to_zip, archiveType)

# Definition of the zip
obj = {
    "inputPath": "/home/vortex/Desktop/LAYERS/ghg/process_data/test_input/COUNTRIES/",
    "outputPath": "/home/vortex/Desktop/LAYERS/ghg/process_data/output/4326/",
    "archiveType": "zip",
    "codingSystem": "faostat",
    # this is done in this case for each country
    "zippit": [
        {
            "name": "FAOSTAT Fire CO2 emission estimates",
            "folderName": "co2_emission_estimates",
            "filename": "co2_emission_estimates",
            "metadataFilesPath": [],
            "folders": [
                "CO2_GFED4BA_Emissions_Burning_ClosedShrublands",
                "CO2_GFED4BA_Emissions_Burning_OpenShrublands",
                ]
        },
        {
            "name": "DM GFED4 burning peatlands",
            "folderName": "dm_gfed4_burning_peatlands",
            "filename": "dm_gfed4_burning_peatlands",
            "metadataFilesPath": [],
            "folders": [
                "DM_GFED4_Burning_Peatlands",
                ]
        },
        {
            "name": "N2O GFED4BA Emissions Burning Peatlands",
            "folderName": "n2o_gfed4ba_emissions_burning_peatlands",
            "filename": "n2o_gfed4ba_emissions_burning_peatlands",
            "metadataFilesPath": [],
            "folders": [
                "N2O_GFED4BA_Emissions_Burning_Peatlands",
                ]
        },
        {
            "name": "GFED4_BurnedArea_Peatlands",
            "folderName": "gfed4_burnedarea_peatlands",
            "filename": "gfed4_burnedarea_peatlands",
            "metadataFilesPath": [],
            "folders": [
                "GFED4_BurnedArea_Peatlands",
                ]
        }
    ]
}


# remove thte output folder and create new output zip files
if os.path.isdir(obj["outputPath"]):
    shutil.rmtree(obj["outputPath"])
createGHGProducts(obj)