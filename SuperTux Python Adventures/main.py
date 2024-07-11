#!/usr/bin/env python3

import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Super Tux Python World')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/Pixeltype.ttf', 69)
fps = 60

pygame.mixer.music.load('instrumental.mp3')
pygame.mixer.music.play()

bg_surface = pygame.image.load('backgrounds/winter1.png').convert()
text_surface = test_font.render('Super Tux: The Python Adventures', False, 'Yellow')

tux_surface = pygame.image.load('Tux/big/idle-0.png').convert_alpha()
tux_rect = tux_surface.get_rect(midbottom = (50,750))

snail_surface = pygame.image.load('snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (1000,750))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bg_surface,(0,0))
    screen.blit(tux_surface,tux_rect)
    screen.blit(text_surface,(250,150))
    screen.blit(snail_surface,snail_rect)
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 1200

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        tux_rect.x -= 4
    if keys[pygame.K_d]:
        tux_rect.x += 4

    if tux_rect.colliderect(snail_rect):
        print('collision')

    pygame.display.update()
    clock.tick(fps)
