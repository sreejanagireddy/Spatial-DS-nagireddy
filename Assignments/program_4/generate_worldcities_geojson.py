import pprint as pp
import os,sys
import json
import collections


f = open("C:\\4553-Spatial-DS\\Resources\\Data\\WorldData\\world_cities_large.json","r")

data = f.read()

data = json.loads(data)

all_world_cities = []


for k,v in data.items():
   
       for i in  v:
       
        gj = collections.OrderedDict()
        gj['type'] = "Feature"
        gj['properties'] = i
        lat = float(i['lat'])
        lon = float(i['lon'])

        del gj['properties']['lat']
        del gj['properties']['lon']
        gj["geometry"] = {}
        gj["geometry"]["type"]="Point"
        gj["geometry"]["coordinates"] = [
          lat,
          lon 
        ]
        all_world_cities.append(gj)
del all_world_cities[999:len(all_world_cities)-1]

#dictionary1['features'] = all_world_cities
out = open("C:\\4553-Spatial-DS\\Resources\\Data\\WorldData\\world_cities_large_gj.geojson","w")

out.write(json.dumps(all_world_cities, sort_keys=False,indent=4, separators=(',', ': ')))

out.close()