import pygame
from tilemaps import *
from random import choice
from itertools import cycle

win = pygame.display.set_mode((1280, 720))
running = True

class Tetrimino:
    def __init__(self, tilemap=tilemap):
        self.shapes = tetrimino_shapes[choice(list(tetrimino_shapes))]
        self.shape = choice(self.shapes)
        self.shapes = cycle(self.shapes)
        self.y = 0
        self.x = 4
        self.tilemap = tilemap
    
    def check_for_collision(self) -> bool:
        '''Checks whether the tetrimino is in overlapping collision with the map'''
        shape = self.shape
        y = 0
        for row in shape:
            x = 0
            for cell in row:
                if self.tilemap[y+self.y][x+self.x] != 0: return True
                x += 1
            y += 1
        
        return False
    
    def __str__(self):
        s = ""
        for row in self.shape:
            for cell in row:
                if cell == 0: s = s + " "
                else: s = s + "O"
            s = s + '\n'
        return str(s)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
    
    pygame.display.update()