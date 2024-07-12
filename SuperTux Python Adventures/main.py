#!/usr/bin/env python3

import pygame
from sys import exit


def display_score():
    current_time = int(pygame.time.get_ticks() / 10) - start_time
    score_surf = test_font.render(f'Score: {current_time}',False,'Yellow')
    score_rect = score_surf.get_rect(center = (1060, 40))
    screen.blit(score_surf,score_rect)

pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Super Tux Python World')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/Pixeltype.ttf', 69)
game_active = True
fps = 60
start_time = 0

pygame.mixer.music.load('music/instrumental.mp3')
pygame.mixer.music.play(-1)

bg_surface = pygame.image.load('images/backgrounds/winter1.png').convert()
text_surface = test_font.render('Super Tux: The Python Adventures', False, 'Yellow')

snail_surface = pygame.image.load('images/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (1000,750))
snail_speed = 4

tux_surface = pygame.image.load('images/Tux/big/idle-0.png').convert_alpha()
tux_rect = tux_surface.get_rect(midbottom = (50,750))
tux_grav = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_active:
        screen.blit(bg_surface,(0,0))
        screen.blit(text_surface,(250,150))
        display_score()

        snail_rect.x -= snail_speed
        if snail_rect.right <= 0: 
            snail_rect.left = 1200
            snail_speed += 1
        screen.blit(snail_surface,snail_rect)

        tux_grav += 1
        tux_rect.y += tux_grav
        if tux_rect.bottom >= 750: tux_rect.bottom = 750
        
        screen.blit(tux_surface,tux_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            tux_rect.x -= 4
        if keys[pygame.K_d]:
            tux_rect.x += 4
        if keys[pygame.K_SPACE] and tux_rect.bottom >= 750:
            tux_grav = -20


        if tux_rect.colliderect(snail_rect):
            game_active = False
            
    else:
        pygame.mixer.music.stop()
        gameover_img = pygame.image.load('images/gameover/gameoverscreen.jpg')
        screen.blit(gameover_img,(0,80))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            game_active = True
            snail_rect.left = 1200
            tux_rect.left = 50
            pygame.mixer.music.play(-1)
            snail_speed = 4
            start_time = int(pygame.time.get_ticks() /10)

    pygame.display.update()
    clock.tick(fps)

