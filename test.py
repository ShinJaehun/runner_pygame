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

sky_surface = pygame.image.load('assets/graphics/Sky.png').convert()
ground_surface = pygame.image.load('assets/graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black')
snail_surface = pygame.image.load('assets/graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	# screen.blit(test_surface, (0, 0))
	
	# 배경이 없으면 snail이 이동하는 과정에서 지워지지 않는다. 결국 매 프레임마다 배경을 새로 그리는 것?
	screen.blit(sky_surface, (0, 0))
	screen.blit(ground_surface, (0, 300))
	screen.blit(text_surface, (300, 50))
	snail_x_pos -= 4
	if (snail_x_pos < -100):
		snail_x_pos = 800
	screen.blit(snail_surface, (snail_x_pos, 250))

	pygame.display.update()
	clock.tick(60)
