import pprint as pp
import os,sys
import json
import collections


f = open("C:\\4553-Spatial-DS\\Resources\\Data\\WorldData\\earthquakes-1960-2017.json","r")

data = f.read()

data = json.loads(data)

all_earthquakes = []



for k,v in data.items():
   
   
    for i in  v:
       
        gj = collections.OrderedDict()
        gj['type'] = "Feature"
        gj['properties'] = i
        gj["geometry"] = {}
        gj["geometry"] = gj['properties']['geometry'] 
        del gj['properties']['geometry']   
        all_earthquakes.append(gj)

del all_earthquakes[999:len(all_earthquakes)-1]


#dictionary1['features'] = all_earthquakes
out = open("C:\\4553-Spatial-DS\\Resources\\Data\\WorldData\\earthquakes.geojson","w")

out.write(json.dumps(all_earthquakes, sort_keys=False,indent=4, separators=(',', ': ')))

out.close()