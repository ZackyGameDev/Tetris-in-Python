import pygame
from tilemaps import *
from definations import *

win = pygame.display.set_mode((1280, 720))
running = True
clock = pygame.time.Clock()
FPS = 10
TILE_SIZE: int = 35
falling = False
dx = 0
active_tetrimino = [Tetrimino(), Tetrimino(), Tetrimino(), Tetrimino()]
board = Board()
fall_timer = FPS

# Temp test surface i use in place of tile sprite till i get actual tile sprites
tile_sprite = pygame.Surface((TILE_SIZE, TILE_SIZE))
pygame.draw.rect(tile_sprite, (255, 255, 255),
                 pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE))
###########################################################################################

while running:
    clock.tick(FPS)  # FPS
    win.fill((0, 0, 0))  # Cleaning the window

    # Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_UP:
                active_tetrimino[0].rotate()
            elif event.key == pygame.K_DOWN:
                falling = True
            elif event.key == pygame.K_SPACE:
                active_tetrimino[0].drop()
                active_tetrimino[0].stop()
                del active_tetrimino[0]
                active_tetrimino.append(Tetrimino())
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dx = 0
            elif event.key == pygame.K_DOWN:
                falling = False

    # Making the tile Move
    fall_timer -= 1
    if fall_timer <= 0 or falling:
        prev_y = active_tetrimino[0].y
        active_tetrimino[0].fall()
        if prev_y == active_tetrimino[0].y:
            active_tetrimino[0].stop()
            del active_tetrimino[0]
            active_tetrimino.append(Tetrimino())
        fall_timer = FPS

    active_tetrimino[0].move_horizontally(dx)

    # Drawing the tilemap
    y = 0
    for row in tilemap:
        x = 0
        for tile in row:
            if tile != 0:
                win.blit(tile_sprite, (x*TILE_SIZE, y*TILE_SIZE))
            else:
                pygame.draw.rect(win, (20, 20, 20), pygame.Rect(
                    x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1

    # Updating the screen
    board.clear_full_rows()
    active_tetrimino[0].draw(TILE_SIZE, {1: tile_sprite}, win)
    pygame.display.update()
