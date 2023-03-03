import pygame
from pygame.constants import KEYDOWN, KEYUP

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Test")
clock = pygame.time.Clock()

#background img
background = pygame.image.load("background.png")

#character init
character = pygame.image.load("character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

character_speed = 1

to_x = 0
to_y = 0

#enemy setting
enemy = pygame.image.load("enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = screen_width / 2 - enemy_width / 2
enemy_y_pos = screen_height / 2 - enemy_height / 2

#handle events
running = True
while running:
    dt = clock.tick(60)
    print("fps: ", clock.get_fps())
    for event in pygame.event.get():
    #    pass
        if event.type == pygame.QUIT:
           running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    character_x_pos += to_x * dt * 0.3
    character_y_pos += to_y * dt * 0.3
    
    #handle border value
    if character_x_pos < 0: character_x_pos = 0
    elif character_x_pos > (screen_width - character_width): character_x_pos = screen_width - character_width
    if character_y_pos < 0: character_y_pos = 0
    elif character_y_pos > (screen_height - character_height): character_y_pos = screen_height - character_height


    #draw
    # screen.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()

pygame.quit()