from queue import PriorityQueue
import pygame
from config.logicConfig import Config


def ucs(maze, start, goal, sc, config=None):
    if config is None:
        config = Config()

    queue = PriorityQueue()
    queue.put((0, start, []))  # Initialize the priority queue with a cost of 0, the start cell, and an empty path

    while not queue.empty():
        cost, current_cell, path = queue.get()

        if current_cell == goal:
            [cell.draw_current_cell(sc) for cell in path]
            # We found the goal, return the path
            return path

        if not current_cell.visited:
            current_cell.visited = True

            # Get neighboring cells
            neighbors = current_cell.find_neighbors(maze)

            for neighbor in neighbors:
                new_cost = cost + 1  # Assuming a uniform cost of 1 for each step
                new_path = path + [current_cell]
                queue.put((new_cost, neighbor, new_path))

        [cell.draw(sc) for cell in maze]
        pygame.display.flip()
        pygame.time.Clock().tick(20)
        pygame.display.update()

    # If no path is found, return None to indicate that there's no solution
    return None