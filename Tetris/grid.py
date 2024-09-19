import pygame
from color import Colors
class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.color = Colors.get_cell_colors()
    
    def is_inside(self, row, col):
        if row >= 0 and row < self.num_rows and col >= 0 and col < self.num_cols:
            return True
        return False
    
    def is_empty(self, col, row):
        if self.grid[row][col] == 0:
            return True
        return False
    
    def is_row_full(self, row):
        for col in range(self.num_cols):
            if self.grid[row][col] == 0:
                return False
        return True
    
    def clear_row(self, row):
        for col in range(self.num_cols):
            self.grid[row][col] = 0
            
    def move_row_down(self, row, num_row):
        for col in range(self.num_cols):
            self.grid[row+num_row][col] = self.grid[row][col]
            self.grid[row][col] = 0
    
    def clear_full_row(self):
        complete = 0
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                complete += 1
            elif complete > 0:
                self.move_row_down(row, complete)
        return complete
                
    def reset(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.grid[row][col] = 0
    
    
    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col*self.cell_size+1, row*self.cell_size+1, self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.color[cell_value], cell_rect)
                