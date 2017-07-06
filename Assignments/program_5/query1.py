import pygame
import math
import pprint as pp
from ast import literal_eval
from pymongo import MongoClient
import os
import sys
from math import radians, cos, sin, asin, sqrt
import string
DIRPATH = os.path.dirname(os.path.realpath(__file__))
client = MongoClient()

def haversine(lon1, lat1, lon2, lat2):
        """
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians 
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 3956 # Radius of earth in kilometers. Use 6371 for km
        return c * r

def mercX(lon):
    """
    Mercator projection from longitude to X coord
    """
    zoom = 1.0
    lon = math.radians(lon)
    a = (256.0 / math.pi) * pow(2.0, zoom)
    b = lon + math.pi
    return int(a * b)


def mercY(lat):
    """
    Mercator projection from latitude to Y coord
    """
    zoom = 1.0
    lat = math.radians(lat)
    a = (256.0 / math.pi) * pow(2.0, zoom)
    b = math.tan(math.pi / 4 + lat / 2)
    c = math.pi - math.log(b)
    return int(a * c)

def get_airports():
    print('hi')
    source_air_code = sys.argv[1]
    dest_air_code = sys.argv[2]
    radius = 500
    res_count = 0
    radius_count = 0
    closest_ap = None
    
    visited = []
    points = []
    visited.append(source_air_code)
    source_cords = get_coords(source_air_code)
    dest_cords = get_coords(dest_air_code)
    dest_lon,dest_lan = dest_cords
    lon,lat = source_cords
    print(lon,lat)
    print(dest_lon,dest_lan)
    for c in range(300):
        min = 999999
        nearby_airports =  client['world_data'].airport.find( { 'geometry': { '$geoWithin': { '$centerSphere': [ [lon, lat] ,float(radius)/3963.2 ] } }} ) 
        res_count = 0
        for ap in nearby_airports:
            #print(ap)
            lon2 = ap['geometry']['coordinates'][0]
            lat2 = ap['geometry']['coordinates'][1]
            distance = haversine(dest_lon,dest_lan,lon2,lat2)
            print(distance)
            if ap['properties']['ap_iata'] not in visited:
                if distance < min:
                    radius = 500
                    radius_count = 0
                    res_count +=1
                    min = distance
                    print(distance)
                    print(ap['properties']['ap_name'])
                    closest_ap = ap
            elif res_count == 0:
                radius +=500
                res_count = 0
                radius_count +=1
                break
        if closest_ap['properties']['ap_iata'] not in visited:
            visited.append(closest_ap['properties']['ap_iata'])
            print('visited is',visited)
            point_lon = closest_ap['geometry']['coordinates'][0]
            point_lat = closest_ap['geometry']['coordinates'][1]
            points.append((point_lon,point_lat))
            lon = closest_ap['geometry']['coordinates'][0]
            lat = closest_ap['geometry']['coordinates'][1]
        print(closest_ap)

        if closest_ap['properties']['ap_iata'] == dest_air_code:
                break
    return points
def getearthquakes(points):
    ear_adjusted=[]
    for p in points:
        air_res = client['world_data'].earthquakes.find( { 'geometry': { '$geoWithin': { '$centerSphere': [ [p[0], p[1] ] , 500/3963.2 ] } }} )
        for coord in air_res:
            lon = float(coord['geometry']['coordinates'][0])
            lat = float(coord['geometry']['coordinates'][1])
            x = int((mercX(lon) / 1024 * 1024))        
            y = int((mercY(lat) / 512 * 512) - 256)     
            ear_adjusted.append((x,y))
    return ear_adjusted    
def getvolcanos(points):
    vol_adjusted=[]
    for p in points:
        air_res_vol = client['world_data'].volcanos.find( { 'geometry': { '$geoWithin': { '$centerSphere': [ [p[0], p[1] ] , 500/3963.2 ] } }} )
        for coord in air_res_vol:
            lon = float(coord['geometry']['coordinates'][0])
            lat = float(coord['geometry']['coordinates'][1])
            x = int((mercX(lon) / 1024 * 1024))        
            y = int((mercY(lat) / 512 * 512) - 256)     
            vol_adjusted.append((x,y))
    return vol_adjusted        
def getmet(points):
    met_adjusted=[]
    for p in points:
        air_res_met = client['world_data'].meteorite.find( { 'geometry': { '$geoWithin': { '$centerSphere': [ [p[0], p[1] ] , 500/3963.2 ] } }} )
        for coord in air_res_met:
            lon = float(coord['geometry']['coordinates'][0])
            lat = float(coord['geometry']['coordinates'][1])
            x = int((mercX(lon) / 1024 * 1024))        
            y = int((mercY(lat) / 512 * 512) - 256)     
            met_adjusted.append((x,y))
    return met_adjusted        
def get_features(points):
    ear_adjusted = []
    vol_adjusted =[]
    met_adjusted = []
    screen_width = 1024
    screen_height = 512
    radius = sys.argv[3]
    final_list = []
   
    ear_adjusted=getearthquakes(points)
    vol_adjusted=getvolcanos(points)    
    met_adjusted=getmet(points)
        
    

def get_coords(value):
    n = None
    result = client['world_data'].ap.find()
    for r in result:
        if r['properties']['ap_iata'] == value:
            lon = r['geometry']['coordinates'][0]
            lat = r['geometry']['coordinates'][1]
            n = lon,lat
            break
        else:
            continue
    return n

def plot_points():
    point = get_airports()
    pts = []
   
    (width, height) = (1024, 512)
    print(len(point))
    for i in point:
        x = int((mercX(i[0]) / 1024 * width))        
        y = int((mercY(i[1]) / 512 * height) - 256)
        pts.append((x,y))
    ear_adjusted=getearthquakes(point)
    vol_adjusted=getvolcanos(point)    
    met_adjusted=getmet(point)
    pp.pprint(ear_adjusted)

    background_colour = (255,255,255)
    
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Query_1')
    screen.fill(background_colour)
    pygame.init()
    bg = pygame.image.load(DIRPATH+'/'+'1024x512.png')
    pygame.display.flip()
            #Json File with all the adjusted coordinates
    running = True
            # c = 1
    while running:
        screen.blit(bg, (0, 0))
        for j in pts:
            pygame.draw.circle(screen, (0,0,255), j, 1,0)
        pygame.draw.lines(screen,(0,0,255),False,pts,3)
        '''
        for d in feature:
            pygame.draw.circle(screen,(0,255,255),d, 1)
            for q in np:
                pygame.draw.circle(screen, (0,255,255), q, 1)
            for r in vol:
                pygame.draw.circle(screen, (194,35,38), r, 1)
            for s in met:
                pygame.draw.circle(screen, (0,255,0), s, 1)
        '''        
        for i in ear_adjusted:
             pygame.draw.circle(screen,(0,255,255),i, 1)  
        for i in vol_adjusted:
             pygame.draw.circle(screen,(255,0,0),i, 1)  
        for i in met_adjusted:
             pygame.draw.circle(screen,(0,255,0),i, 1)                 
           
            
          
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clean_area(screen,(0,0),width,height,(255,255,255))
            if event.type == pygame.QUIT:
                pygame.image.save(screen,DIRPATH+'/'+'query1_ScreenShot.png')
                running = False
        pygame.display.flip()



if __name__=='__main__':
    plot_points()
