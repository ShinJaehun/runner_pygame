from cgi import test
import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('assets/font/Pixeltype.ttf', 50)
# test_surface = pygame.Surface((100, 200))
# test_surface.fill('Red')

sky_surface = pygame.image.load('assets/graphics/Sky.png')
ground_surface = pygame.image.load('assets/graphics/ground.png')
text_surface = test_font.render('My game', False, 'Black')

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	# screen.blit(test_surface, (0, 0))
	
	screen.blit(sky_surface, (0, 0))
	screen.blit(ground_surface, (0, 300))
	screen.blit(text_surface, (300, 50))

	pygame.display.update()
	clock.tick(60)
