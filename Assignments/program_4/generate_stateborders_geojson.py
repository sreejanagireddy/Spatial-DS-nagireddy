import pprint as pp
import os,sys
import json
import collections


f = open("C:\\4553-Spatial-DS\\Resources\\Data\\WorldData\\state_borders.json","r")

data = f.read()

data = json.loads(data)

all_state_borders = []


for k in data:
   
    gj = collections.OrderedDict()
    gj['type'] = "Feature"
    gj['properties'] = k
  
    borders = k['borders']
 
    del gj['properties']['borders']
    gj["geometry"] = {}
    gj["geometry"]["type"]="Polygon"
    gj["geometry"]["coordinates"] = borders
      
    all_state_borders.append(gj)

del all_state_borders[999:len(all_state_borders)-1]

#dictionary1['features'] = all_state_borders
out = open("C:\\4553-Spatial-DS\\Resources\\Data\\WorldData\\state_borders_gj.geojson","w")

out.write(json.dumps(all_state_borders, sort_keys=False,indent=4, separators=(',', ': ')))

out.close()