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



def createGHGProductsGlobal(obj):
    inputPath = obj["inputPath"]
    outputPath = obj["outputPath"]
    archiveType = obj["archiveType"]
    zips = obj["zippit"]

    # create the zip files
    for to_zip in zips:
        print to_zip["name"]
        outputFilename = to_zip["filename"]
        outputFolderName = to_zip["folderName"]

        # TODO: get all country codes (to be used in the folder input construction)

        # TODO add to the path gaul code i.e. 4326/product/faostat/12/product_name.zip
        # Create Product
        outputFolderPath = os.path.join(outputPath, outputFolderName)
        if not os.path.isdir(outputFolderPath):
            os.makedirs(outputFolderPath)

        outputFilePath = os.path.join(outputFolderPath, outputFilename)

        # delete file if already exists
        if os.path.isfile(outputFilePath):
            os.remove(outputFilePath)

        folders_to_zip = []
        for folder in to_zip["folders"]:
            # TODO add to the path gaul code i.e. inputPath/12/inputFolder
            folders_to_zip.append(os.path.join(inputPath, folder))

        # create zip file
        createZip(outputFilePath, folders_to_zip, archiveType)


# Definition of the zip
objCountry = {
    "inputPath": "/home/vortex/Desktop/LAYERS/ghg/geodata_handedoverto_simonem_052015/4326_download/COUNTRIES",
    "outputPath": "/home/vortex/Desktop/LAYERS/ghg/download/4326/",
    "archiveType": "zip",
    "codingSystem": "faostat",
    # this is done in this case for each country
    "zippit": [
        {
            "name": "GFED4 burned areas",
            "folderName": "GFED4_burned_areas",
            "filename": "GFED4_burned_areas",
            "metadataFilesPath": [],
            "folders": ["GFED4 burned areas"]
        },
        {
            "name": "Burned dry matter",
            "folderName": "Burned_dry_matter",
            "filename": "Burned_dry_matter",
            "metadataFilesPath": [],
            "folders": ["Burned dry matter"]
        },
        {
            "name": "Organic soils area",
            "folderName": "Organic_soils_area",
            "filename": "Organic_soils_area",
            "metadataFilesPath": [],
            "folders": ["Organic soils area"]
        },
        {
            "name": "Climate",
            "folderName": "Climate",
            "filename": "Climate",
            "metadataFilesPath": [],
            "folders": ["Climate"]
        },
        {
            "name": "Ecology",
            "folderName": "Ecology",
            "filename": "Ecology",
            "metadataFilesPath": [],
            "folders": ["Ecology"]
        },
        {
            "name": "Livestock",
            "folderName": "Livestock",
            "filename": "Livestock",
            "metadataFilesPath": [],
            "folders": ["Livestock"]
        },
        {
            "name": "Land Cover",
            "folderName": "Land_Cover",
            "filename": "Land_Cover",
            "metadataFilesPath": [],
            "folders": ["Land Cover"]
        },
        {
            "name": "FAOSTAT fire CO2 emission estimates",
            "folderName": "FAOSTAT_fire_CO2_emission_estimates",
            "filename": "FAOSTAT_fire_CO2_emission_estimates",
            "metadataFilesPath": [],
            "folders": ["FAOSTAT fire CO2 emission estimates"]
        },
        {
            "name": "FAOSTAT fire N2O emission estimates",
            "folderName": "FAOSTAT_fire_N2O_emission_estimates",
            "filename": "FAOSTAT_fire_N2O_emission_estimates",
            "metadataFilesPath": [],
            "folders": ["FAOSTAT fire N2O emission estimates"]
        },
        {
            "name": "FAOSTAT fire CH4 emission estimates",
            "folderName": "FAOSTAT_fire_CH4_emission_estimates",
            "filename": "FAOSTAT_fire_CH4_emission_estimates",
            "metadataFilesPath": [],
            "folders": ["FAOSTAT fire CH4 emission estimates"]
        },
        {
            "name": "FAOSTAT cultivation of organic soil CO2 emission estimates",
            "folderName": "FAOSTAT_cultivation_of_organic_soil_CO2_emission_estimates",
            "filename": "FAOSTAT_cultivation_of_organic_soil_CO2_emission_estimates",
            "metadataFilesPath": [],
            "folders": ["FAOSTAT cultivation of organic soil CO2 emission estimates"]
        },
        {
            "name": "FAOSTAT cultivation of organic soil N2O emission estimates",
            "folderName": "FAOSTAT_cultivation_of_organic_soil_N2O_emission_estimates",
            "filename": "FAOSTAT_cultivation_of_organic_soil_N2O_emission_estimates",
            "metadataFilesPath": [],
            "folders": ["FAOSTAT cultivation of organic soil N2O emission estimates"]
        }
    ]
}



objGlobal = {
    # "inputPath": "/home/vortex/Desktop/LAYERS/ghg/process_data/test_input/COUNTRIES/",
    "inputPath": "/home/vortex/Desktop/LAYERS/ghg/geodata_handedoverto_simonem/4326/",
    "outputPath": "/home/vortex/Desktop/LAYERS/ghg/process_data/output/4326/",
    "archiveType": "zip",
    # "codingSystem": "faostat",
    # this is done in this case for each country
    "zippit": [
        {
            "name": "FAOSTAT Fire CO2 emission estimates",
            "folderName": "co2_emission_estimates",
            "filename": "co2_emission_estimates",
            "metadataFilesPath": [],
            "folders": [
                # "CO2_GFED4BA_Emissions_Burning_ClosedShrublands",
                # "CO2_GFED4BA_Emissions_Burning_OpenShrublands",
                "CO2_Emissions_Burning_ClosedShrublands",
                "CO2_Emissions_Burning_OpenShrublands",
            ]
        },
        {
            "name": "DM GFED4 burning peatlands",
            "folderName": "dm_gfed4_burning_peatlands",
            "filename": "dm_gfed4_burning_peatlands",
            "metadataFilesPath": [],
            "folders": [
                # "DM_GFED4_Burning_Peatlands",
                "DM_Burning_Peatlands",
            ]
        },
        {
            "name": "N2O GFED4BA Emissions Burning Peatlands",
            "folderName": "n2o_gfed4ba_emissions_burning_peatlands",
            "filename": "n2o_gfed4ba_emissions_burning_peatlands",
            "metadataFilesPath": [],
            "folders": [
                # "N2O_GFED4BA_Emissions_Burning_Peatlands",
                "N2O_Emissions_Burning_Peatlands",
            ]
        },
        {
            "name": "GFED4_BurnedArea_Peatlands",
            "folderName": "gfed4_burnedarea_peatlands",
            "filename": "gfed4_burnedarea_peatlands",
            "metadataFilesPath": [],
            "folders": [
                # "GFED4_BurnedArea_Peatlands",
                "GFED4_BurnedAreas_Peatlands",
            ]
        }
    ]
}


# remove thte output folder and create new output zip files
if os.path.isdir(objCountry["outputPath"]):
    shutil.rmtree(objCountry["outputPath"])

print "Creating by contry products"
createGHGProducts(objCountry)

# print "Creating by global products"
# createGHGProductsGlobal(objGlobal)