import pygame
from random import choice

from config.config import STARTCOLOR, VISITEDCOLOR, BORDERCOLOR
from config.logicConfig import Config


class Cell:
    def __init__(self, x, y, map_size=None, config=None):
        if config is None:
            config = Config()
        self.x, self.y = x, y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.size = map_size
        self.visited = False
        self.thickness = 4
        self.cel_size = config.cellsize

    def draw_current_cell(self, sc, color=None):
        if color is None:
            color = STARTCOLOR
        x, y = self.x * self.cel_size, self.y * self.cel_size
        pygame.draw.rect(sc, pygame.Color(color), (x + 2, y + 2, self.cel_size - 2, self.cel_size - 2))

    def draw(self, sc):
        x, y = self.x * self.cel_size, self.y * self.cel_size
        if self.visited:
            pygame.draw.rect(sc, pygame.Color(VISITEDCOLOR), (x + 2, y + 2, self.cel_size - 2, self.cel_size - 2))

        if self.walls['top']:
            pygame.draw.line(sc, pygame.Color(BORDERCOLOR), (x, y), (x + self.cel_size, y), self.thickness)
        else:
            pygame.draw.line(sc, pygame.Color(VISITEDCOLOR), (x, y), (x + self.cel_size, y), self.thickness)
        if self.walls['right']:
            pygame.draw.line(sc, pygame.Color(BORDERCOLOR), (x + self.cel_size, y),
                             (x + self.cel_size, y + self.cel_size),
                             self.thickness)
        else:
            pygame.draw.line(sc, pygame.Color(VISITEDCOLOR), (x + self.cel_size, y),
                             (x + self.cel_size, y + self.cel_size),
                             self.thickness)

        if self.walls['bottom']:
            pygame.draw.line(sc, pygame.Color(BORDERCOLOR), (x + self.cel_size, y + self.cel_size),
                             (x, y + self.cel_size),
                             self.thickness)
        else:
            pygame.draw.line(sc, pygame.Color(VISITEDCOLOR), (x + self.cel_size, y + self.cel_size),
                             (x, y + self.cel_size),
                             self.thickness)
        if self.walls['left']:
            pygame.draw.line(sc, pygame.Color(BORDERCOLOR), (x, y + self.cel_size), (x, y), self.thickness)
        else:
            pygame.draw.line(sc, pygame.Color(VISITEDCOLOR), (x, y + self.cel_size), (x, y), self.thickness)

    def possible_move(self, grid_cells):
        self.grid_cells = grid_cells
        neighbors = {}
        top = self.check_cell(self.x, self.y - 1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)
        if not self.walls['top'] and top:
            neighbors['top'] = top
        if not self.walls['right'] and right:
            neighbors['right'] = right
        if not self.walls['bottom'] and bottom:
            neighbors['bottom'] = bottom
        if not self.walls['left'] and left:
            neighbors['left'] = left
        return neighbors

    def check_cell(self, x, y):
        cols, rows = self.size
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
        return neighbors
