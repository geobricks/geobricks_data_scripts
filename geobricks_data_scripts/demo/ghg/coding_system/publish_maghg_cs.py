import glob
import os
import csv

files = glob.glob("/home/vortex/Desktop/LAYERS/GHG_13_NOVEMEBRE/MAGHG-data/OUTPUT/*.tif")

cached_codes = []
codes = []
for f in files:
    if "_3857" in f:
        if "20" in f or "19" in f:
            # it contains a date
            folder, filename = os.path.split(f.rsplit("_", 2)[0])
        else:
            folder, filename = os.path.split(f.rsplit("_", 1)[0])
        if filename not in cached_codes:
            cached_codes.append(filename)
            codes.append([filename.lower().replace(" ","_"), filename.replace("_", " ")])


with open('csv/cs_maghg.csv', 'wb') as csvfile:
    w = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for code in codes:
        w.writerow(code)


