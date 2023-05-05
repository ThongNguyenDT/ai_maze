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


