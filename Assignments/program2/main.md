```py
"""
Program:
--------
    Program 2

Description:
------------
    This programe takes each row from given files and considers only x and y co-ordinates 
	to display points on screen.Each file is read with different method which scales x and
	y co-ordinates to fit on screen.    
Name: Sreeja Nagireddy
Date: 19 june 2017
"""

import pygame
import random
from dbscan import *
import sys,os
import pprint as pp


class crime(object):

	def __init__(self):
        
		keys = []
		crimes=[]
		self.DIRPATH = os.path.dirname(os.path.realpath(__file__))
		self.got_keys = False
		#with open(DIRPATH+'/../NYPD_CrimeData/Nypd_Crime_01') as f:
		self.file1=[]
		self.file2=[]
		self.file3=[]
		self.file4=[]
		self.file5=[]
		
		
		

		epsilon = 20
		min_pts = 5

		
	
	def manhattan(self):
		

		keys = []
		crimes=[]

		with open(self.DIRPATH+'/filtered_crimes_manhattan.csv') as f:
			for line in f:
				line = ''.join(x if i % 2 == 0 else x.replace(',', ':') for i, x in enumerate(line.split('"')))
				line = line.strip().split(',')
				if not self.got_keys:
					keys = line
					print(keys)
					self.got_keys = True
					continue
				crimes.append(line)
		self.got_keys = False
		points=[]	
		MaxX= 1067226
		MaxY=271820
		MinX=913357
		MinY= 121250 

		for crime in crimes:
			if len(crime) == 24:
				if len(crime[19]) != 0 and len(crime[20]) != 0:
					x = crime[19]
					y = crime[20]

					x10=int(x)
					y10=int(y)
					points.append((x10,y10))


		for value in points:

			x= (value[0]-MinX)/(MaxX-MinX)
			y=(value[1]-MinY)/(MaxY-MinY)

			self.file1.append((x*1000,(1-y)*1000))

	def	bronx(self):
	 
	
		keys = []
		crimes=[] 
		with open(self.DIRPATH+'/filtered_crimes_bronx.csv') as f:
			for line in f:
				line = ''.join(x if i % 2 == 0 else x.replace(',', ':') for i, x in enumerate(line.split('"')))
				line = line.strip().split(',')
				if not self.got_keys:
					keys = line
					print(keys)
					self.got_keys = True
					continue
				crimes.append(line)
			self.got_keys = False
		points=[]	
		MaxX= 1067226
		MaxY=271820
		MinX=913357
		MinY= 121250 
		
		for crime in crimes:
			if len(crime) == 24:
				if len(crime[19]) != 0 and len(crime[20]) != 0:
					x = crime[19]
					y = crime[20]
					x10=int(x)
					y10=int(y)
					points.append((x10,y10))
		 

		for value in points:
			
			x= (value[0]-MinX)/(MaxX-MinX)
			y=(value[1]-MinY)/(MaxY-MinY)
			
			self.file2.append((x*1000,(1-y)*1000))
			

		
	def island(self):	
	
		keys = []
		crimes=[]
		with open(self.DIRPATH+'/filtered_crimes_staten_island.csv') as f:
			for line in f:
				line = ''.join(x if i % 2 == 0 else x.replace(',', ':') for i, x in enumerate(line.split('"')))
				line = line.strip().split(',')
				if not self.got_keys:
					keys = line
					print(keys)
					self.got_keys = True
					continue
				crimes.append(line)
			self.got_keys = False
		points=[]	
		MaxX= 1067226
		MaxY=271820
		MinX=913357
		MinY= 121250 
		
		for crime in crimes:
			if len(crime) == 24:
				if len(crime[19]) != 0 and len(crime[20]) != 0:
					x = crime[19]
				   
					y = crime[20]
				
					x10=int(x)
					y10=int(y)
					points.append((x10,y10))
		 

		for value in points:
			
			x= (value[0]-MinX)/(MaxX-MinX)
			y=(value[1]-MinY)/(MaxY-MinY)
			
			self.file3.append((x*1000,(1-y)*1000))
	def queens(self):	
	

	
		keys = []
		crimes=[]
		with open(self.DIRPATH+'/filtered_crimes_queens.csv') as f:
			for line in f:
				line = ''.join(x if i % 2 == 0 else x.replace(',', ':') for i, x in enumerate(line.split('"')))
				line = line.strip().split(',')
				if not self.got_keys:
					keys = line
					print(keys)
					self.got_keys = True
					continue
				crimes.append(line)
			self.got_keys = False
		points=[]	
		MaxX= 1067226
		MaxY=271820
		MinX=913357
		MinY= 121250 
		
		for crime in crimes:
			if len(crime) == 24:
				if len(crime[19]) != 0 and len(crime[20]) != 0:
					x = crime[19]
					y = crime[20]
					x10=int(x)
					y10=int(y)
					points.append((x10,y10))
		 

		for value in points:
			
			x= (value[0]-MinX)/(MaxX-MinX)
			y=(value[1]-MinY)/(MaxY-MinY)
			
			self.file4.append((x*1000,(1-y)*1000))
			
	def brooklyn(self):
	
	
		keys = []
		crimes=[]
		with open(self.DIRPATH+'/filtered_crimes_brooklyn.csv') as f:
			for line in f:
				line = ''.join(x if i % 2 == 0 else x.replace(',', ':') for i, x in enumerate(line.split('"')))
				line = line.strip().split(',')
				if not self.got_keys:
					keys = line
					print(keys)
					self.got_keys = True
					continue
				crimes.append(line)
			self.got_keys = False
		points=[]	
		MaxX= 1067226
		MaxY=271820
		MinX=913357
		MinY= 121250 
		
		for crime in crimes:
			if len(crime) == 24:
				if len(crime[19]) != 0 and len(crime[20]) != 0:
					x = crime[19]
				   # print(x)
					y = crime[20]
					#print(y)
					x10=int(x)
					y10=int(y)
					points.append((x10,y10))
		 

		for value in points:
			
			x= (value[0]-MinX)/(MaxX-MinX)
			y=(value[1]-MinY)/(MaxY-MinY)
			
			self.file5.append((x*1000,(1-y)*1000))
			
if __name__ == "__main__":		

	running = True
	count=0
	c=crime()
	
	c.manhattan()
	c.bronx()
	c.brooklyn()
	c.queens()
	c.island()
	background_colour = (255,255,255)
	black = (0,0,0)
	(width, height) = (1000, 1000)

	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption('Program2')
	screen.fill(background_colour)

	pygame.display.flip()
	
 
	epsilon = 20
	min_pts = 5
	while running:
		pygame.init()
		myfont = pygame.font.SysFont(None,56)
		text = myfont.render("sreeja Nagireddy",True,black)
		screen.blit(text,(0,20))
		
		for p in c.file1:
			pygame.draw.circle(screen,(194,35,38), (int(p[0]),int(p[1])), 3, 0)
		for p in c.file2:
			pygame.draw.circle(screen, (2,120,120), (int(p[0]),int(p[1])), 3, 0)
		for p in c.file3:
			pygame.draw.circle(screen, (253,182,50), (int(p[0]),int(p[1])), 3, 0)
		for p in c.file4:
			pygame.draw.circle(screen, (243,115,56), (int(p[0]),int(p[1])), 3, 0)	
		for p in c.file5:
			pygame.draw.circle(screen, (128,22,56), (int(p[0]),int(p[1])), 3, 0)	
		pygame.image.save(screen , "crime.png")	
		pygame.display.flip()
```
