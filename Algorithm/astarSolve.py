import pygame
import heapq
from config.logicConfig import Config
from config.config import *
from object.gameplay.Cell import Cell

size = INIT_WIDTH // CELLSIZE, INIT_HEIGHT // CELLSIZE
cols, rows = size
Igrid_cells = [Cell(col, row, size) for row in range(rows) for col in range(cols)]


class AStarMAPGen:
    def __init__(self, grid_cells=None, config=None):
        if grid_cells is None:
            grid_cells = Igrid_cells
        if config is None:
            config = Config()
        self.config = config
        self.size = self.config.width // self.config.cellsize, self.config.heigh // self.config.cellsize
        self.grid_cells = grid_cells
        self.colors, self.color = [], 40
        self.pq = []  # Priority queue for A* Search

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
        heapq.heappush(self.pq, (0, 0, current_cell))  # Push the starting cell with priority 0 and cost 0
        array = []
        break_count = 1

        while break_count != len(grid_cells):
            _, _, next_cell = heapq.heappop(self.pq)  # Pop the cell with the highest priority and cost
            if next_cell:
                break_count += 1
                array.append(current_cell)
                self.remove_walls(current_cell, next_cell)
                current_cell = next_cell
            elif array:
                current_cell = array.pop()
            current_cell.visited = True

            neighbors = current_cell.check_neighbors(self.grid_cells)
            for neighbor in neighbors:
                cost = 1  # Replace with your specific cost function
                heuristic_cost = self.heuristic(neighbor)
                total_cost = cost + heuristic_cost
                heapq.heappush(self.pq, (total_cost, cost, neighbor))

        return grid_cells

    def draw_maze(self, sc, current_cell, isBreak=False):
        current_cell.visited = True
        current_cell.draw_current_cell(sc)
        [pygame.draw.rect(sc, self.colors[i],
                          (cell.x * self.config.cellsize + 5, cell.y * self.config.cellsize + 5,
                           self.config.cellsize - 10, self.config.cellsize - 10),
                          border_radius=8) for i, (_, _, cell) in enumerate(self.pq)]
        _, _, next_cell = heapq.heappop(self.pq)  # Pop the cell with the highest priority and cost
        if next_cell:
            self.pq.append((self.calculate_priority(next_cell), self.calculate_cost(next_cell), next_cell))
            self.colors.append((min(self.color, 255), 10, 100))
            self.color += 1
            self.remove_walls(current_cell, next_cell)
            current_cell = next_cell
        elif not self.pq:
            isBreak = True

        return current_cell, isBreak

    def heuristic(self, cell):
        # Replace with your specific heuristic function, e.g., Manhattan distance to the goal
        return abs(cell.x - (self.size[0] - 1)) + abs(cell.y - (self.size[1] - 1))

    def calculate_priority(self, cell):
        # Replace with your specific calculation for priority
        return self.calculate_cost(cell) + self.heuristic(cell)

    def calculate_cost(self, cell):
        # Replace with your specific cost function
        return 1
