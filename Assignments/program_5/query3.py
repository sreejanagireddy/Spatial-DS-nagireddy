import math
import os
import sys
import pygame
import pprint as pprint
from pymongo import MongoClient
from dbscan import *
from map_helper import *
DIRPATH = os.path.dirname(os.path.realpath(__file__))
client = MongoClient()

def find_extremes(result_list,width,height):
    extremes={}
    points = []
    allx = []
    ally = []
    points = []
    
    for r in result_list:
        lon = r['geometry']['coordinates'][0]
        lat = r['geometry']['coordinates'][1]
        x,y = (mercX(lon),mercY(lat))
        allx.append(x)
        ally.append(y)
        points.append((x,y))
    extremes['max_x'] = width
    extremes['min_x'] = 0
    extremes['max_y'] = height
    extremes['min_y'] = 0
    extremes['max_x'] = width
    extremes['min_x'] = 0
    extremes['max_y'] = height
    extremes['min_y'] = 0
    return extremes,points
epsilon = sys.argv[3]
width,height = 1024,512
min_points = int(sys.argv[2])
x = {}
count = 5
y = []
findrect = []
feature = sys.argv[1]
if feature == 'meteorite':
    air_res = client['world_data'][feature].find({'properties.mass':{'$gt' : ('90000')}})
    x,y = find_extremes(air_res,width,height)
elif feature == 'volcanos':
    air_res = client['world_data'][feature].find()
    x,y = find_extremes(air_res,width,height)
elif feature == 'earthquakes':
    air_res = client['world_data'][feature].find({'properties.mag':{'$gt' : (7.5)}})
    x,y = find_extremes(air_res,width,height)
y = adjust_location_coords(x,y,width,height)
cal_mbrs = calculate_mbrs(y,epsilon,min_points)
sorted(cal_mbrs,key = len)
for i in range(0,6):
    findrect.append(cal_mbrs[i])
background_colour = (255,255,255)
black = (0,0,0)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Query_3')
screen.fill(background_colour)
pygame.init()
bg = pygame.image.load(DIRPATH+'/'+'1024x512.png')
pygame.display.flip()
    #Json File with all the adjusted coordinates
running = True
    # c = 1
while running:
    screen.blit(bg, (0, 0))
    for rec in findrect:
        pygame.draw.polygon(screen,(0,255,0),rec,1)
       # pygame.display.flip()
    for p in y:
        pygame.draw.circle(screen,(255,0,0), p, 1,1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.QUIT:
            pygame.image.save(screen,DIRPATH+'/'+'EarthQuake_ScreenShot.png')
            running = False
    
       # pygame.display.flip()
            
    pygame.display.flip()
