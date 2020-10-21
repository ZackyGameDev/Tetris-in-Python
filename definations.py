import pygame
from tilemaps import *
from random import choice

class Board:
	def __init__(self, tilemap:list=tilemap):
		self.tilemap:list = tilemap
		
	def clear_full_rows(self):
		y = 0
		empty_row = []
		for i in range(10):
			empty_row.append(0)
		for row in tilemap:
			if not 0 in row:
				del tilemap[y]
				tilemap.insert(0, empty_row)
			y += 1

	def __str__(self):
		s = ""
		for row in self.tilemap:
			for cell in row:
				if cell == 0: s = s + " "
				else: s = s + "XX"
			s = s + '\n'
		return str(s)				

class Tetrimino:
	def __init__(self, tilemap=tilemap):
		self.shapes : list = tetrimino_shapes[choice(list(tetrimino_shapes))]
		self.shape : list = choice(self.shapes)
		self.y = 0
		self.x = 4
		self.tilemap : list = tilemap
		if self.colliding_with_map():
			pygame.quit()
	
	def draw(self, tile_size:int, tile_sprites_dict:dict, display_to_draw_to):
		y = 0
		for row in self.shape:
			x = 0
			for tile in row:
				if tile != 0: display_to_draw_to.blit(tile_sprites_dict[tile], ((x+self.x)*tile_size, (y+self.y)*tile_size))
				x += 1
			y += 1
			
	
	def colliding_with_map(self, shape=None) -> bool:
		'''Checks whether the tetrimino is in overlapping collision with the map, Also checks if the tetrimino is out of the map or not'''
		if shape == None:
			shape = self.shape
		y = 0
		for row in shape:
			x = 0
			for tile in row:
				if tile != 0:
					try:
						if tilemap[y+self.y][x+self.x] != 0 or self.x+x < 0:
							return True
					except IndexError:
						return True
				x += 1
			y += 1
		
		return False
	
	def drop(self):
		'''Same as self.fall() but instantly makes the thing fall, rather than making it fall one tile'''
		while not self.colliding_with_map():
			self.y += 1
		self.y -= 1
	
	def stop(self) -> None:
		shape = self.shape
		tilemap = self.tilemap
		y = 0
		for row in shape:
			x = 0
			for tile in row:
				if tile != 0:
					tilemap[y+self.y][x+self.x] = tile
				x += 1
			y += 1
	
	def will_collide_after_rotation(self) -> bool:
		'''Checks whether the tetrimino is in overlapping collision with the map if it were to be rotated'''
		try:
			shape : list = self.shapes[self.shapes.index(self.shape)+1]
		except IndexError:
			shape : list = self.shapes[0]
		
		return self.colliding_with_map(shape=shape)
	
	def move_horizontally(self, direction:int):
		'''Moves the tetrimino right or left, based on the direction provided to move in, 
		direction=1 for right and -1 for left, collision is handled inside this function itself'''
		if not self.colliding_with_map():
			self.x += direction
		if self.colliding_with_map():
			self.x -= direction
		
	def rotate(self):
		'''Rotates the tetrimino, i.e., changes the shape to next(shapes)'''
		if not self.will_collide_after_rotation():
			try:
				self.shape : list = self.shapes[self.shapes.index(self.shape)+1]
			except IndexError:
				self.shape : list = self.shapes[0]
		
	def fall(self):
		'''similar to `self.move_horizontally()` but moves the tetrimino vertically down instead'''
		if not self.colliding_with_map():
			self.y += 1
		if self.colliding_with_map():
			self.y -= 1

	def __str__(self):
		s = ""
		for row in self.shape:
			for cell in row:
				if cell == 0: s = s + " "
				else: s = s + "XX"
			s = s + '\n'
		return str(s)
	
if __name__ == '__main__':
	__import__('tetris')