import pygame


class Ship:

	def __init__(self, screen):
		self.screen = screen
		self.image = pygame.image.load("ship.png")  
		self.rectangle = self.image.get_rect()
		self.rectangle.midbottom = self.screen.get_rect().midbottom
		self.moving_left = False #new
		self.moving_right = False #new

	def draw_ship(self):
		self.screen.blit(self.image, self.rectangle)

	def move_left(self):
		self.rectangle.x = self.rectangle.x - 2

	def move_right(self):
		self.rectangle.x = self.rectangle.x + 2

	def move(self):
		if self.moving_right == True:
			self.rectangle.x = self.rectangle.x + 2
		if self.moving_left == True:
			self.rectangle.x = self.rectangle.x - 2
		
