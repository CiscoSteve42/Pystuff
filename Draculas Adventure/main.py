#!/usr/bin/env python3

import pygame


pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Dracula\'s Adventure')
clock = pygame.time.Clock()
game_font = pygame.font.Font('font/Pixeltype.ttf', 69)
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

title_text = game_font.render('Dracula\'s Adventure', False, "#F1FA8C")
title_rect = title_text.get_rect(center = (640,150))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('#BD93F9')
    pygame.draw.rect(screen,'#6272A4',title_rect)
    screen.blit(title_text,title_rect)
    pygame.draw.circle(screen, '#50FA7B', player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
