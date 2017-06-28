import pprint as pp
import os,sys
import json
import collections


f = open("C:\\4553-Spatial-DS\\Resources\\Data\\WorldData\\world_volcanos.json","r")

data = f.read()

data = json.loads(data)

all_world_volcanos = []



for k in data:
   
    gj = collections.OrderedDict()
    gj['type'] = "Feature"
    gj['properties'] = k
    if len(k['Lat']) != 0:
      Lat = float(k['Lat'])
      Lon = float(k['Lon'])
 
    del gj['properties']['Lat']
    del gj['properties']['Lon']
   
    gj["geometry"] = {}
    gj["geometry"]["type"]="Point"
    gj["geometry"]["coordinates"] = [
          Lon,
          Lat 
    ]
    all_world_volcanos.append(gj)
del all_world_volcanos[999:len(all_world_volcanos)-1]    
out = open("C:\\4553-Spatial-DS\\Resources\\Data\\WorldData\\valcanos_gj.geojson","w")

out.write(json.dumps(all_world_volcanos, sort_keys=False,indent=4, separators=(',', ': ')))

out.close()