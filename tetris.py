import pygame

pygame.display.set_mode((600, 360))
game_is_running = True

# Game Loop
while game_is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False
