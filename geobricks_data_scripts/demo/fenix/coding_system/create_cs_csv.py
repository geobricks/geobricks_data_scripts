import csv

items = [
        "Cultivation Organic Soils",
        "GFED4 Burned Areas",
        "GFED4 Burned Areas - Barren or sparsely vegetated",
        "GFED4 Burned Areas - Closed shrubland",
        "GFED4 Burned Areas - Croplands",
        "GFED4 Burned Areas - Deciduous Broadleaf forest",
        "GFED4 Burned Areas - Deciduous Needleleaf forest",
        "GFED4 Burned Areas - Evergreen Broadleaf forest",
        "GFED4 Burned Areas - Evergreen Needleleaf forest",
        "GFED4 Burned Areas - Grassland",
        "GFED4 Burned Areas - Humid Tropical Forest",
        "GFED4 Burned Areas - Mixed forest",
        "GFED4 Burned Areas - Open shrubland",
        "GFED4 Burned Areas - Organic soils",
        "GFED4 Burned Areas - Other forest",
        "GFED4 Burned Areas - Savanna",
        "GFED4 Burned Areas - Unclassified",
        "GFED4 Burned Areas - Urban and built-up",
        "GFED4 Burned Areas - Woody savanna",
        "Global Ecological Zones (GEZ) 2010",
        "Global Land Cover 2000 (GLC2000)",
        "Gridded Livestock of the World v. 2.01",
        "Harmonized World Soil Database - Organic soils",
        "JRC climate zone",
        "JRC climate zone (4326)",
        "MODIS - Land Cover Type UMD"
]


final = []
with open('csv/cs_ghg.csv', 'wb') as csvfile:
        w = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in items:
            s = i.lower().replace(" ", "_")
            w.writerow([s, i])
            final.append([s, i])
print final








