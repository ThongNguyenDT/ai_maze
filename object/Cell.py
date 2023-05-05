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


