import pygame
from random import choice
from config.config import INIT_WIDTH, CELLSIZE, INIT_HEIGHT

cols, rows = INIT_WIDTH // CELLSIZE, INIT_HEIGHT // CELLSIZE

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False
        self.thickness = 4

    def draw(self, sc):
        x, y = self.x * CELLSIZE, self.y * CELLSIZE

        if self.walls['top']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x, y), (x + CELLSIZE, y), self.thickness)
        if self.walls['right']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x + CELLSIZE, y), (x + CELLSIZE, y + CELLSIZE), self.thickness)
        if self.walls['bottom']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x + CELLSIZE, y + CELLSIZE), (x , y + CELLSIZE), self.thickness)
        if self.walls['left']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x, y + CELLSIZE), (x, y), self.thickness)

    def get_rects(self):
        rects = []
        x, y = self.x * CELLSIZE, self.y * CELLSIZE
        if self.walls['top']:
            rects.append(pygame.Rect( (x, y), (CELLSIZE, self.thickness) ))
        if self.walls['right']:
            rects.append(pygame.Rect( (x + CELLSIZE, y), (self.thickness, CELLSIZE) ))
        if self.walls['bottom']:
            rects.append(pygame.Rect( (x, y + CELLSIZE), (CELLSIZE , self.thickness) ))
        if self.walls['left']:
            rects.append(pygame.Rect( (x, y), (self.thickness, CELLSIZE) ))
        return rects

    def check_cell(self, x, y):
        find_index = lambda x, y: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return self.grid_cells[find_index(x, y)]

    def check_neighbors(self, grid_cells):
        self.grid_cells = grid_cells
        neighbors = []
        top = self.check_cell(self.x, self.y - 1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return choice(neighbors) if neighbors else False
