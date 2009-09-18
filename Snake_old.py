import pygame, sys, random, time
from pygame.locals import *

U, D, L, R = 1, 2, 3, 4

class Map:
	name = "Default"
	startPos = [(11, 10), (12, 10), (13, 10)]
	startDir = R
	speed = "1.0/(self.score+5)"
	def mapp(self):
		return [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],	# 22x19 map
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

class Snake:
	def __init__(self, mapPath=None):
		if mapPath:
			self.mapp = Map(mapPath)
		else:
			self.mapp = Map()
				
		self.surface = self.mapp.mapp()
		self.snake = self.mapp.startPos
		self.headPos = self.snake[len(self.snake)-1]
		
		self.score = 0
		
		pygame.init()
		self.window = pygame.display.set_mode((len(self.surface)*23+3, len(self.surface[0])*23+3)) # +20 for stat bar
		pygame.display.set_caption("Sneaky Snaky")
		self.screen = pygame.display.get_surface()
		
	def drawRect(self, x, y, color):
		pygame.draw.rect(self.screen, color, (x*23+3, y*23+3, 20, 20)) # +20 for stat bar

	def printSurface(self):
		self.surface[self.apple[0]][self.apple[1]] = 2 # DO APPLE
		for x in range(len(self.surface)):
			for y in range(len(self.surface[x])):
				if self.surface[x][y] == 0:		# Nothing
					self.drawRect(x, y, (0, 0, 0))
				if self.surface[x][y] == 1:		# Wall
					self.drawRect(x, y, (0, 0, 225))
				if self.surface[x][y] == 2:		# Apple
					self.drawRect(x, y, (225, 0, 0))
				if self.surface[x][y] == 3:		# Snake
					self.drawRect(x, y, (225, 225, 225))
				if self.surface[x][y] == 4:		# Head of snake
					self.drawRect(x, y, (225, 0, 225))
	
	def printStats(self):
		"""pygame.draw.rect(self.screen, (225, 225, 225), (3, 3, len(self.surface)*23-3, 17))
		pygame.display.flip()
		self.font = pygame.font.Font("ProggyTiny.fon", 22)
		text = self.font.render(str(self.score) + " apples eaten", False, (0, 0, 0), (225, 225, 225))
		self.screen.blit(text, (len(self.surface)*23-3-text.get_width(), 6))
		text = self.font.render("\"" + self.mapp.name + "\"", False, (0, 0, 0), (225, 225, 225))
		self.screen.blit(text, (6, 6))"""
		pygame.display.set_caption("Sneaky Snaky ["+str(self.score)+"]")
	
	def drawApple(self):
		x, y = random.choice(range(22)), random.choice(range(19))
		while self.surface[x][y] != 0:
			x, y = random.choice(range(22)), random.choice(range(19))
		self.apple = (x, y)
		
	def move(self, dir):
		if dir == U:
			self.snake.append( (self.headPos[0], self.headPos[1]-1) )
		if dir == D:
			self.snake.append( (self.headPos[0], self.headPos[1]+1) )
		if dir == L:
			self.snake.append( (self.headPos[0]-1, self.headPos[1]) )
		if dir == R:
			self.snake.append( (self.headPos[0]+1, self.headPos[1]) )
		self.headPos = self.snake[len(self.snake)-1]
		
	def drawSnake(self):
		self.surface = self.mapp.mapp()
		if len(self.snake) > self.score+3:
			self.snake.pop(0)
		for part in self.snake:
			self.surface[part[0]][part[1]] = 3
		self.surface[self.headPos[0]][self.headPos[1]] = 4
	
	def checkCollision(self):
		headPosValue = self.surface[self.headPos[0]][self.headPos[1]]
		if headPosValue != 0:
			if headPosValue == 2: # == eat apple
				self.score += 1
				self.drawApple()
				return False
			if headPosValue != 4: # other collisions == DEATH
				return True
	
	def quit(self):
		print "\nYou died fool! You ate " + str(self.score) + " apples\n"
		sys.exit(0)
	
	def play(self):
		self.drawSnake()
		self.drawApple()
		self.printSurface()
		self.printStats()
		pygame.display.flip()
		direction = olDir = self.mapp.startDir
		
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					self.quit()
				if event.type == KEYDOWN:
					if event.key == 119 and event.mod == 1024:
						self.quit()
					if event.key == K_UP and olDir != D:
						direction = U
					if event.key == K_DOWN and olDir != U:
						direction = D
					if event.key == K_LEFT and olDir != R:
						direction = L
					if event.key == K_RIGHT and olDir != L:
						direction = R
				else:
					pass
			
			self.move(direction)
			olDir = direction
			if self.checkCollision():
				self.quit()
			
			self.drawSnake()
			self.printSurface()
			self.printStats()
			pygame.display.flip()
			time.sleep(eval(self.mapp.speed))
			
game = Snake()
game.play()