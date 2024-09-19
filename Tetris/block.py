from color import Colors
from position import Position
import pygame

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.col_offset = 0
        self.rotation_state = 0
        self.color = Colors.get_cell_colors()
        
    def move(self, row, col):
        self.row_offset += row
        self.col_offset += col
        
    def get_cell_posotion(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for postition in tiles:
            postition = Position(postition.row + self.row_offset, postition.col + self.col_offset)
            moved_tiles.append(postition)
        return moved_tiles
    
    def rotate(self):
        self.rotation_state = (self.rotation_state + 1) % 4
    
    def undo_rotate(self):
        self.rotation_state -= 1
        if self.rotation_state < 0:
            self.rotation_state = 3
        
    def draw(self, screen):
        tiles = self.get_cell_posotion()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.col * self.cell_size+1, tile.row * self.cell_size+1, self.cell_size-1, self.cell_size-1)
            pygame.draw.rect(screen, self.color[self.id], tile_rect)
        