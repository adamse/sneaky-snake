import pygame, sys, random, time
from pygame.locals import *

U, D, L, R = 1, 2, 3, 4

class Map:
	name = "Default"
	def startPos(self):
		return [(11, 10), (12, 10), (13, 10)]
	def mapp(self):
		return [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
		[1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],]

class Snake:
	def __init__(self, mapPath=None):
		if mapPath:
			self.mapp = Map(mapPath)
		else:
			self.mapp = Map()
				
		self.surface = self.mapp.mapp()
		self.snake = self.mapp.startPos()
		self.headPos = self.snake[len(self.snake)-1]
		
		self.score = 0
		
		pygame.init()
		self.window = pygame.display.set_mode((len(self.surface[0])*20, len(self.surface)*20)) 
		pygame.display.set_caption("Sneaky Snaky")
		self.screen = pygame.display.get_surface()
		
	def drawRect(self, x, y, color):
		pygame.draw.rect(self.screen, color, (x*20, y*20, 20, 20)) 

	def printSurface(self):
		self.surface[self.apple[1]][self.apple[0]] = 2 # DO APPLE
		for y in range(len(self.surface)):
			for x in range(len(self.surface[y])):
				if self.surface[y][x] == 0:		# Nothing
					self.drawRect(x, y, (0, 0, 0))
				if self.surface[y][x] == 1:		# Wall
					self.drawRect(x, y, (0, 0, 225))
				if self.surface[y][x] == 2:		# Apple
					self.drawRect(x, y, (225, 0, 0))
				if self.surface[y][x] == 3:		# Snake
					self.drawRect(x, y, (225, 225, 225))
				if self.surface[y][x] == 4:		# Head of snake
					self.drawRect(x, y, (225, 0, 225))
	
	def printStats(self):
		"""pygame.draw.rect(self.screen, (225, 225, 225), (0, 0, len(self.surface)*20, 20))
		pygame.display.flip()
		self.font = pygame.font.Font(None, 22)
		text = self.font.render(str(self.score) + " apples eaten", False, (0, 0, 0), (225, 225, 225))
		self.screen.blit(text, (len(self.surface)*23-3-text.get_width(), 6))
		text = self.font.render("\"" + self.mapp.name + "\"", False, (0, 0, 0), (225, 225, 225))
		self.screen.blit(text, (6, 6))"""
		pygame.display.set_caption("Sneaky Snaky ["+str(self.score)+"]")
	
	def drawApple(self):
		x, y = random.choice(range(len(self.surface[0]))), random.choice(range(len(self.surface)))
		while self.surface[y][x] != 0:
			x, y = random.choice(range(len(self.surface[0]))), random.choice(range(len(self.surface)))
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
		if len(self.snake) > self.score+len(self.mapp.startPos()):
			self.snake.pop(0)
		for part in self.snake:
			self.surface[part[1]][part[0]] = 3
		self.surface[self.headPos[1]][self.headPos[0]] = 4
	
	def checkCollision(self):
		headPosValue = self.surface[self.headPos[1]][self.headPos[0]]
		if headPosValue != 0:
			if headPosValue == 2: # == eat apple
				self.score += 1
				self.drawApple()
				return False
			if headPosValue != 4: # other collisions == DEATH
				return True
	
	def quit(self):
		self.time = round(time.time()-self.timer, 1)
		print "\nYou died fool! You ate %d apples in %.1f seconds" % (self.score, self.time)
		sys.exit(0) 
		
	def play(self):
		if len(sys.argv) > 1:
			self.speed = int(sys.argv[1])
			if self.speed <= 5:
				self.speed = 5
			if self.speed > 99:
				self.speed = 99
		else:
			self.speed = 10
		
		pygame.mouse.set_visible(False)
		
		self.drawSnake()
		self.drawApple()
		self.printSurface()
		self.printStats()
		pygame.display.flip()
		direction = olDir = R
		
		self.timer = time.time()
		
		while True:
			for event in pygame.event.get():
				if event.type == QUIT: # Pressing close button
					self.quit()
				if event.type == KEYDOWN:
					if event.key == 119 and event.mod == 1024: # Cmd+w for quit
						self.quit()
					
					
					if event.key == K_UP and olDir != D:
						direction = U
					if event.key == K_DOWN and olDir != U:
						direction = D
					if event.key == K_LEFT and olDir != R:
						direction = L
					if event.key == K_RIGHT and olDir != L:
						direction = R
					
					if event.key == 45: # Change speed by +/- keys
						self.speed += 1
					if event.key == 47:
						self.speed -= 1
				else:
					pass
			
			if pygame.key.get_focused():
				self.move(direction)
				olDir = direction
			
			if self.checkCollision():
				self.quit()
			
			self.drawSnake()
			self.printSurface()
			self.printStats()
			pygame.display.flip()
			if self.speed <= 0:
				self.speed = 1
			elif self.speed >= 100:
				self.speed = 99
			pygame.time.delay(1000/self.speed)
			

game = Snake()
game.play()