import os
import glob

def rename_burned_areas_folders(folder):
    folders = glob.glob(os.path.join(folder, "*"))
    print folders
    for folder in folders:
        print folder
        if os.path.isdir(folder):
            product_code = os.path.basename(os.path.normpath(folder))
            print product_code
            product_name = burned_areas_folder(product_code)

            print


def burned_areas_folder(folder):
    filename = folder.lower()
    if "peatlands" in filename:
        return "GFED4 Burned Areas - Organic soils"
    if "AllForestsMinus".lower() in filename:
        return "GFED4 Burned Areas - Other forest"
    if "humidtropicalforests".lower() in filename:
        return "GFED4 Burned Areas - Humid Tropical Forest"

    burned_areas_lc = "GFED4 Burned Areas - "
    if "1" in filename:
        return burned_areas_lc + "Evergreen Needleleaf forest"
    if "2" in filename:
        return burned_areas_lc + "Evergreen Broadleaf forest"
    if "3" in filename:
        return burned_areas_lc + "Deciduous Needleleaf forest"
    if "4" in filename:
        return burned_areas_lc + "Deciduous Broadleaf forest"
    if "5" in filename:
        return burned_areas_lc + "Mixed forest"
    if "6" in filename:
        return burned_areas_lc + "Closed shrubland"
    if "7" in filename:
        return burned_areas_lc + "Open shrubland"
    if "8" in filename:
        return burned_areas_lc + "Woody savanna"
    if "9" in filename:
        return burned_areas_lc + "Savanna"
    if "10" in filename:
        return burned_areas_lc + "Grassland"
    if "12" in filename:
        return burned_areas_lc + "Croplands"
    if "13" in filename:
        return burned_areas_lc + "Urban and built-up"
    if "16" in filename:
        return burned_areas_lc + "Barren or sparsely vegetated"
    if "17" in filename:
        return burned_areas_lc + "Unclassified"

def burned_areas_switch(filename):
    filename = filename.lower()
    if "peatlands" in filename:
        return "GFED4 Burned Areas - Organic soils"
    if "AllForestsMinus".lower() in filename:
        return "GFED4 Burned Areas - Other forest"
    if "humidtropicalforests".lower() in filename:
        return "GFED4 Burned Areas - Humid Tropical Forest"

    burned_areas_lc = "GFED4 Burned Areas - "
    if "lc_1_" in filename:
        return burned_areas_lc + "Evergreen Needleleaf forest"
    if "lc_2_" in filename:
        return burned_areas_lc + "Evergreen Broadleaf forest"
    if "lc_3_" in filename:
        return burned_areas_lc + "Deciduous Needleleaf forest"
    if "lc_4_" in filename:
        return burned_areas_lc + "Deciduous Broadleaf forest"
    if "lc_5_" in filename:
        return burned_areas_lc + "Mixed forest"
    if "lc_6_" in filename:
        return burned_areas_lc + "Closed shrubland"
    if "lc_7_" in filename:
        return burned_areas_lc + "Open shrubland"
    if "lc_8_" in filename:
        return burned_areas_lc + "Woody savanna"
    if "lc_9_" in filename:
        return burned_areas_lc + "Savanna"
    if "lc_10_" in filename:
        return burned_areas_lc + "Grassland"
    if "lc_12_" in filename:
        return burned_areas_lc + "Croplands"
    if "lc_13_" in filename:
        print filename
        return burned_areas_lc + "Urban and built-up"
    if "lc_16_" in filename:
        return burned_areas_lc + "Barren or sparsely vegetated"
    if "lc_17_" in filename:
        return burned_areas_lc + "Unclassified"


rename_burned_areas_folders("/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/Theory_structure_novemeber_13/GFED4_BURNEDAREAS_BY_LANDCOVER/")