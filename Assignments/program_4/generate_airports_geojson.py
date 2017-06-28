import pprint as pp
import os,sys
import json
import collections


f = open("C:\\4553-Spatial-DS\\Resources\\Data\\WorldData\\airports.json","r")

data = f.read()

data = json.loads(data)

all_airports = []
  
for k,v in data.items():
   
    gj = collections.OrderedDict()
    gj['type'] = "Feature"
    gj['properties'] = v
    lat = v['lat']
    lon = v['lon']
    del gj['properties']['lat']
    del gj['properties']['lon']
    gj["geometry"] = {}
    gj["geometry"]["type"]="Point"
    gj["geometry"]["coordinates"] = [
          lon,
          lat
        ]
    all_airports.append(gj)
del all_airports[999:len(all_airports)-1]


out = open("C:\\4553-Spatial-DS\\Resources\\Data\\WorldData\\airports1_gj.geojson","w")

out.write(json.dumps(all_airports, sort_keys=False,indent=4, separators=(',', ': ')))

out.close()