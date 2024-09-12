import pygame


class Bullet:

	def __init__(self, screen, myship):
		self.speed = 5
		self.damge = 25
		self.color = (255, 255, 255)
		self.width = 10
		self.height = 10
		self.screen = screen
		self.rectangle = pygame.Rect(0, 0, self.height, self.width)
		self.rectangle.midtop = myship.rectangle.midtop
		#self.rectangle.midtop = (200, 200)

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rectangle)

	def move_bullet(self):
		self.rectangle.y = self.rectangle.y - 1
