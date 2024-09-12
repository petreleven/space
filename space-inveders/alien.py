import pygame

class Alien:
  def __init__(self, screen):
    self.speed = 1
    self.image = pygame.image.load("alien.png")
    self.screen = screen
    self.rectangle = self.image.get_rect()
    self.rectangle.center = (50, 50) 
    self.visible = True
    

    
  def show_alien(self):
    if self.visible == True:
      self.screen.blit(self.image, self.rectangle)

  def move(self):
    self.rectangle.y = self.rectangle.y + 1