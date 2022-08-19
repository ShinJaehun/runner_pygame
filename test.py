from cgi import test
import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('assets/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('assets/graphics/Sky.png').convert()
ground_surface = pygame.image.load('assets/graphics/ground.png').convert()

score_surf = test_font.render('My game', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('assets/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('assets/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.blit(sky_surface, (0, 0))
	screen.blit(ground_surface, (0, 300))

	# 근데 rect 마진을 위해서 이렇게 두번 호출해야 하는게.... 맞는거야?
	pygame.draw.rect(screen, '#c0e8ec', score_rect)
	pygame.draw.rect(screen, '#c0e8ec', score_rect, 20)
	# pygame.draw.line(screen, 'Gold', (0,0), (800, 400), 10)
	# pygame.draw.line(screen, 'Gold', (0,0), pygame.mouse.get_pos(), 10)
	# pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50, 200, 100, 100))

	screen.blit(score_surf, score_rect)
	
	snail_rect.x -= 4
	if (snail_rect.right <= 0):
		snail_rect.left = 800
	screen.blit(snail_surf, snail_rect)
	screen.blit(player_surf, player_rect)

	pygame.display.update()
	clock.tick(60)
