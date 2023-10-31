import pygame
from config.logicConfig import Config


def greedy(maze, start, goal, sc, config=None):
    if config is None:
        config = Config()
    print('hear')
    queue = [(start, [])]  # Initialize the queue with the start cell and an empty path

    while queue:
        current_cell, path = queue[
            0]  # Get the current cell and its path (Greedy selects the "best" based on heuristic)

        if current_cell == goal:
            [cell.draw_current_cell(sc) for cell in path]
            # We found the goal, return the path
            return path

        if not current_cell.visited:
            current_cell.visited = True

            # Get neighboring cells
            neighbors = current_cell.find_neighbors(maze)

            # Sort neighbors by a heuristic (e.g., distance to the goal)
            neighbors.sort(key=lambda neighbor: heuristic(neighbor, goal))

            for neighbor in neighbors:
                new_path = path + [current_cell]
                queue.append((neighbor, new_path))

        [cell.draw(sc) for cell in maze]
        pygame.display.flip()
        pygame.time.Clock().tick(20)
        pygame.display.update()

        queue.pop(0)  # Remove the first element (Greedy doesn't use a deque)

    # If no path is found, return None to indicate that there's no solution
    return None


def heuristic(cell, goal):
    # Replace with your specific heuristic function, e.g., Manhattan distance
    return abs(cell.x - goal.x) + abs(cell.y - goal.y)

# The remaining code (import statements and non-algorithm-related parts) remains unchanged.
