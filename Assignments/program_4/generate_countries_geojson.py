import pprint as pp
import os,sys
import json
import collections


f = open("C:\\4553-Spatial-DS\\Resources\\Data\\WorldData\\countries.geo.json","r")

data = f.read()

data = json.loads(data)

all_countries = []

for i in data:
    gj = collections.OrderedDict()
    gj = i
    all_countries.append(gj)

del all_countries[999:len(all_countries)-1]


out = open("C:\\4553-Spatial-DS\\Resources\\Data\\WorldData\\countries_gj.geojson","w")

out.write(json.dumps(all_countries, sort_keys=False,indent=4, separators=(',', ': ')))

out.close()