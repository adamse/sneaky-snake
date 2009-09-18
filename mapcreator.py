import pygame, sys, random, time
from pygame.locals import *

class createMap:
	mapp = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
				[1, 0, 0, 0, 0, 0, 0, 0, 3, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
				[1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],]
	
	def __init__(self):
		if (len(sys.argv) != 3):
			print """Usage createmap x-size y-size mapname"""
			exit(1)
		pygame.init()
		self.xsize = int(sys.argv[1])
		self.ysize = int(sys.argv[2])
		self.window = pygame.display.set_mode((self.xsize*20, self.ysize*20)) 
		pygame.display.set_caption("Sneaky Snaky: Map Creator")
		self.screen = pygame.display.get_surface()

		self.mapp = [[1]*self.xsize]
		for i in range(self.ysize-2):
			self.mapp.append([1]+[0]*(self.xsize-2)+[1])
		self.mapp.append([1]*self.xsize)
		
		self.snake = [(self.xsize/2-1, self.ysize/2),(self.xsize/2, self.ysize/2),(self.xsize/2+1, self.ysize/2)]
		print self.snake, len(self.mapp), len(self.mapp[0])
		self.drawSnake()
		self.printSurface()
		pygame.display.flip()
		
	def drawSnake(self):
		head = self.snake.pop(-1)
		for part in self.snake:
			self.mapp[part[1]][part[0]] = 3
		self.mapp[head[1]][head[0]] = 4
	
	def drawRect(self, x, y, color):
		pygame.draw.rect(self.screen, color, (x*20, y*20, 20, 20)) 
	
	def printSurface(self):
		for y in range(len(self.mapp)):
			for x in range(len(self.mapp[y])):
				if self.mapp[y][x] == 0:		# Nothing
					self.drawRect(x, y, (0, 0, 0))
				if self.mapp[y][x] == 1:		# Wall
					self.drawRect(x, y, (0, 0, 225))
				#if self.mapp[y][x] == 2:		# Apple
				#	self.drawRect(x, y, (225, 0, 0))
				if self.mapp[y][x] == 3:		# Snake
					self.drawRect(x, y, (225, 225, 225))
				if self.mapp[y][x] == 4:		# Head of snake
					self.drawRect(x, y, (225, 0, 225))	
	def quit(self):
		sys.exit(0)
	
	def do(self):
		while True:
			for event in pygame.event.get():
				if event.type == QUIT: # Pressing close button
					self.quit()
				if event.type == KEYDOWN:
					if event.key == 119 and event.mod == 1024: # Cmd+w for quit
						self.quit()
				if event.type == MOUSEBUTTONDOWN:
					x = event.pos[0]/20
					y = event.pos[1]/20
					print event, x, y
					if event.button == 1:
						self.mapp[y][x] = 1
					if event.button == 3:
						self.mapp[y][x] = 0
				else:
					pass
			self.printSurface()
			pygame.display.flip()
				
		

game = createMap()
game.do()