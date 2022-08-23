from cgi import test
import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		player_walk1 = pygame.image.load('assets/graphics/Player/player_walk_1.png').convert_alpha()
		player_walk2 = pygame.image.load('assets/graphics/Player/player_walk_2.png').convert_alpha()
		self.player_walk = [player_walk1, player_walk2]
		self.player_index = 0
		self.jump = pygame.image.load('assets/graphics/Player/jump.png').convert_alpha()
		self.image = self.player_walk[self.player_index]
		self.rect = self.image.get_rect(midbottom = (80, 300))
		self.gravity = 0
	def player_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
			self.gravity = -20
	def apply_gravity(self):
		self.gravity += 1
		self.rect.y += self.gravity
		if self.rect.bottom >= 300: self.rect.bottom = 300
	def animation_state(self):
		if self.rect.bottom < 300:
			self.image = self.jump
		else:
			self.player_index += 0.1
			if self.player_index >= len(self.player_walk): self.player_index = 0
			self.image = self.player_walk[int(self.player_index)]
	def update(self):
		self.player_input()
		self.apply_gravity()
		self.animation_state()

class Obstacle(pygame.sprite.Sprite):
	def __init__(self, type):
		super().__init__()
		if type == 'fly':
			fly_frame1 = pygame.image.load('assets/graphics/Fly/Fly1.png').convert_alpha()
			fly_frame2 = pygame.image.load('assets/graphics/Fly/Fly2.png').convert_alpha()
			self.frames = [fly_frame1, fly_frame2]
			y_pos = 210
		else:
			snail_frame_1 = pygame.image.load('assets/graphics/snail/snail1.png').convert_alpha()
			snail_frame_2 = pygame.image.load('assets/graphics/snail/snail2.png').convert_alpha()
			self.frames = [snail_frame_1, snail_frame_2]
			y_pos = 300
		self.animation_index = 0
		self.image = self.frames[self.animation_index]
		self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))
	def animation_state(self):
		self.animation_index += 0.1
		if self.animation_index >= len(self.frames): self.animation_index = 0
		self.image = self.frames[int(self.animation_index)]		
	def update(self):
		self.animation_state()
		self.rect.x -= 6
		self.destroy()
	def destroy(self):
		if self.rect.x <= -100:
			self.kill()

def display_score():
	current_time = int(pygame.time.get_ticks() / 1000) - start_time
	score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
	score_rect = score_surf.get_rect(center = (400, 50))
	screen.blit(score_surf, score_rect)
	return current_time

# def obstacle_movement(obstacle_list):
# 	if obstacle_list:
# 		for obstacle_rect in obstacle_list:
# 			obstacle_rect.x -= 5
# 			if obstacle_rect.bottom == 300:
# 				screen.blit(snail_surf, obstacle_rect)
# 			else:
# 				screen.blit(fly_surf, obstacle_rect)
# 		obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
# 		return obstacle_list
# 	else: return []

# def collision(player, obstacles):
# 	if obstacles:
# 		for obstacle_rect in obstacles :
# 			if player.colliderect(obstacle_rect):
# 				return False
# 	return True

def collision_sprite():
	if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
		obstacle_group.empty()
		return False
	else: return True

# def player_animation():
# 	global player_surf, player_index
# 	# 이것도 이런 식으로 정의하는게 좀 그런데....
# 	if player_rect.bottom < 300:
# 		player_surf = player_jump
# 	else:
# 		# 프레임에 따라서 0.1씩 주다가 1이 되면 다음 애니메이션으로 넘어가는건가?
# 		# 정확히 알려면 player_index 값을 print해보면 된다.
# 		print(player_index)
# 		player_index += 0.1 
# 		if player_index >= len(player_walk): player_index = 0
# 		player_surf = player_walk[int(player_index)]

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('assets/font/Pixeltype.ttf', 50)

game_active = False
start_time = 0
score = 0

# groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load('assets/graphics/Sky.png').convert()
ground_surface = pygame.image.load('assets/graphics/ground.png').convert()

# # obstacles
# snail_frame_1 = pygame.image.load('assets/graphics/snail/snail1.png').convert_alpha()
# snail_frame_2 = pygame.image.load('assets/graphics/snail/snail2.png').convert_alpha()
# snail_frames = [snail_frame_1, snail_frame_2]
# snail_frame_index = 0
# snail_surf = snail_frames[snail_frame_index]
# fly_frame1 = pygame.image.load('assets/graphics/Fly/Fly1.png').convert_alpha()
# fly_frame2 = pygame.image.load('assets/graphics/Fly/Fly2.png').convert_alpha()
# fly_frames = [fly_frame1, fly_frame2]
# fly_frame_index = 0
# fly_surf = fly_frames[fly_frame_index]

# obstacle_rect_list = []

# player_walk1 = pygame.image.load('assets/graphics/Player/player_walk_1.png').convert_alpha()
# player_walk2 = pygame.image.load('assets/graphics/Player/player_walk_2.png').convert_alpha()
# player_walk = [player_walk1, player_walk2]
# player_index = 0
# player_jump = pygame.image.load('assets/graphics/Player/jump.png').convert_alpha()
# player_surf = player_walk[player_index]
# player_rect = player_surf.get_rect(midbottom = (80, 300))

# player_gravity = 0

# intro screen
player_stand = pygame.image.load('assets/graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render('Press space to run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 320))

# timer
obstacle_timer = pygame.USEREVENT + 1
# set_timer 뒤에 숫자는 ms를 의미하는가?
pygame.time.set_timer(obstacle_timer, 1500)

# 이건 좀 아쉬운데 강사 선생님이 refactoring하면서 각 obstacle의 timer를 어떻게 적용하는지 설명 안해주셨다.
# 아마 Class내에 type에 따라 timer를 설정하고 event가 발생함에 따라 어떻게 처리해야 할꺼 아닌가?

# snail_animation_timer = pygame.USEREVENT + 2
# pygame.time.set_timer(snail_animation_timer, 500)

# fly_animation_timer = pygame.USEREVENT + 3
# pygame.time.set_timer(fly_animation_timer, 200)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

		# if game_active:
		# 	if event.type == pygame.MOUSEBUTTONDOWN:
		# 		if player_rect.collidepoint(event.pos): 
		# 			player_gravity = -20
		# 	if event.type == pygame.KEYDOWN:
		# 		if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
		# 			player_gravity = -20
		# else:
		# 	if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
		# 		game_active = True
		# 		start_time = int(pygame.time.get_ticks() / 1000)

		if not game_active and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
			game_active = True
			start_time = int(pygame.time.get_ticks() / 1000)

		if game_active:
			if event.type == obstacle_timer:
				obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
				# if randint(0, 2):
				# 	obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900, 1100), 300)))
				# else:
				# 	obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900, 1100), 210)))

			# if event.type == snail_animation_timer:
			# 	if snail_frame_index == 0: snail_frame_index = 1
			# 	else: snail_frame_index = 0
			# 	snail_surf = snail_frames[snail_frame_index]
			# if event.type == fly_animation_timer:
			# 	if fly_frame_index == 0: fly_frame_index = 1
			# 	else: fly_frame_index = 0
			# 	fly_surf = fly_frames[fly_frame_index]

	if game_active:
		screen.blit(sky_surface, (0, 0))
		screen.blit(ground_surface, (0, 300))

		score = display_score()

		# player
		# player_gravity += 1
		# player_rect.y += player_gravity
		# if player_rect.bottom >= 300: player_rect.bottom = 300
		# player_animation()
		# screen.blit(player_surf, player_rect)
		# ㅋㅋㅋ
		player.draw(screen)
		player.update()

		obstacle_group.draw(screen)
		obstacle_group.update()

		# obstacle movement
		# obstacle_rect_list = obstacle_movement(obstacle_rect_list)

		# collision
		# game_active = collision(player_rect, obstacle_rect_list)
		game_active = collision_sprite()
	else:
		screen.fill((94, 129, 162))
		screen.blit(player_stand, player_stand_rect)
		# obstacle_rect_list.clear()
		# player_rect.midbottom = (80,300)
		# player_gravity = 0

		score_message = test_font.render(f'Your score: {score}', False, (111, 196, 169))
		score_message_rect = score_message.get_rect(center = (400, 330))

		screen.blit(game_name, game_name_rect)

		if score == 0:
			screen.blit(game_message, game_message_rect)
		else:
			screen.blit(score_message, score_message_rect)

	pygame.display.update()
	clock.tick(60)
