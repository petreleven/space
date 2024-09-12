import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien
#the size of our screen
width = 400
height = 400
#create  screen
screen = pygame.display.set_mode((width, height))
Clock = pygame.time.Clock()

myship = Ship(screen=screen)
mybullet = Bullet(screen=screen, myship=myship)
background_color = [50, 50, 50]  #247 , 0
list_of_bullets = []  #CONTAINER  TO HOLD ALL OUR BULLETS
single_alien = Alien(screen=screen)  #SINGLE ALIEN
#new -creating our aliens
list_of_aliens = []
for number in range(5):
	new_alien = Alien(screen=screen)
	new_alien.rectangle.x = new_alien.rectangle.x + 80 * number
	list_of_aliens.append(new_alien)


def handle_input():
	for event in pygame.event.get():
		#DETECT IF WE RELEASE A KEY
		if event.type == pygame.KEYUP: #new
			if event.key == pygame.K_LEFT:#new
				

		
			
		if event.type == pygame.KEYDOWN:
			background_color = [66, 135, 245]

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				myship.moving_left = True
				myship.moving_right = False

			if event.key == pygame.K_RIGHT:
				myship.moving_right = True
				myship.moving_left = False

			
			if event.key == pygame.K_SPACE:
				#CREATE A NEW BULLET AND SAVE IT IN THE LIST
				newbullet = Bullet(screen=screen, myship=myship)
				list_of_bullets.append(newbullet)


#play the game continuosly
while True:
	myship.move()
	#detect input from player
	handle_input()
	screen.fill(background_color)
	myship.draw_ship()
	#mybullet.draw_bullet()
	#mybullet.move_bullet
	for bullet in list_of_bullets:
		bullet.draw_bullet()
		bullet.move_bullet()

	for alien in list_of_aliens:
		alien.show_alien()
		#alien.move()

	#new content
	for alien in list_of_aliens:
		for bullet in list_of_bullets:
			#TODO alien should check if hit by any of the bullet
			result = alien.rectangle.colliderect(bullet.rectangle)
			if result == True:
				alien.visible = False

	#end new content

	single_alien.show_alien()
	pygame.display.flip()
	Clock.tick(120)
