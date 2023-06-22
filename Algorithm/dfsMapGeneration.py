import pygame

from config.logicConfig import Config
from config.config import *
from object.gameplay.Cell import Cell

size = INIT_WIDTH // CELLSIZE, INIT_HEIGHT // CELLSIZE
cols, rows = size
Igrid_cells = [Cell(col, row, size) for row in range(rows) for col in range(cols)]


class DFSMAPGen:
    def __init__(self, grid_cells=None):
        if grid_cells is None:
            grid_cells = Igrid_cells
        config = Config()
        self.size = config.width // config.cellsize(), config.heigh // config.cellsize()
        self.grid_cells = grid_cells
        self.colors, self.color = [], 40
        self.stack = []

    def remove_walls(self, current, next):
        dx = current.x - next.x
        if dx == 1:
            current.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1:
            current.walls['right'] = False
            next.walls['left'] = False
        dy = current.y - next.y
        if dy == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False

    def generate_maze_nodraw(self):
        rows, cols = self.size
        grid_cells = [Cell(col, row, self.size) for row in range(rows) for col in range(cols)]
        current_cell = grid_cells[0]
        array = []
        break_count = 1

        while break_count != len(grid_cells):
            current_cell.visited = True
            next_cell = current_cell.check_neighbors(grid_cells)
            if next_cell:
                next_cell.visited = True
                break_count += 1
                array.append(current_cell)
                self.remove_walls(current_cell, next_cell)
                current_cell = next_cell
            elif array:
                current_cell = array.pop()
        return grid_cells

    def draw_maze(self, sc, current_cell):
        current_cell.visited = True
        current_cell.draw_current_cell(sc)
        [pygame.draw.rect(sc, self.colors[i],
                          (cell.x * CELLSIZE + 5, cell.y * CELLSIZE + 5, CELLSIZE - 10, CELLSIZE - 10),
                          border_radius=12) for i, cell in enumerate(self.stack)]
        next_cell = current_cell.check_neighbors(self.grid_cells)
        if next_cell:
            next_cell.visited = True
            self.stack.append(current_cell)
            self.colors.append((min(self.color, 255), 10, 100))
            self.color += 1
            self.remove_walls(current_cell, next_cell)
            current_cell = next_cell
        elif self.stack:
            current_cell = self.stack.pop()

        return current_cell
