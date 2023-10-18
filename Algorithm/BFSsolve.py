import os

import numpy as np

from config.logicConfig import Config


class BFS:
    def __init__(self, grid_cells, size, current_cell, config=None):
        if config is None:
            config = Config()
        self.config = config
        self.size = size[1], size[0]  # 0 cols, 1 rows
        self.maze = np.array(grid_cells).reshape(self.size).tolist()
        self.current_cell = current_cell
        self.end = (size[1] - 1, size[0] - 1)
        self.colors, self.color = [], 40
        self.queue = [self.current_cell]
        self.path = []

    def solve_maze_bfs(self, maze, draw):
        print(self.size)
        self.maze = np.array(maze).reshape(self.size).tolist()
        rows, cols = len(self.maze), len(self.maze[0])
        start = (0, 0)
        end = (rows - 1, cols - 1)

        stack = [start]
        visited = set()
        maze_copy = [row[:] for row in self.maze]  # Create a copy of the maze

        step = 1

        while stack:
            current = stack.pop()
            x, y = current

            # Mark the current cell as part of the path
            maze_copy[x][y] = 2

            # Clear the console (for better visualization)
            os.system("cls" if os.name == "nt" else "clear")

            # Print the step number
            print("Step {}:".format(step))


            if current == end:
                break  # Stop if the end is reached

            step += 1

            # Try moving up
            if x > 0 and self.maze[x - 1][y] == 0 and (x - 1, y) not in visited:
                stack.append((x - 1, y))
                visited.add((x - 1, y))

            # Try moving down
            if x < rows - 1 and self.maze[x + 1][y] == 0 and (x + 1, y) not in visited:
                stack.append((x + 1, y))
                visited.add((x + 1, y))

            # Try moving left
            if y > 0 and self.maze[x][y - 1] == 0 and (x, y - 1) not in visited:
                stack.append((x, y - 1))
                visited.add((x, y - 1))

            # Try moving right
            if y < cols - 1 and self.maze[x][y + 1] == 0 and (x, y + 1) not in visited:
                stack.append((x, y + 1))
                visited.add((x, y + 1))

            # for i in visited:
            #     self.maze[i[0] * rows + i[1]].visited = True
            # draw()

        return maze_copy

    def draw_maze(self, queue, isBreak=False):
        self.queue = queue
        if not self.queue:
            isBreak = True
            return
        self.current_cell = self.queue.pop(0)
        if not self.current_cell.visited:
            self.current_cell.visited = True
            self.path.append(self.current_cell)
            queue.extend(self.current_cell.check_neighbors)


if __name__ == '__main__':

    # Example maze
    maze = [
        [0, 0, 1, 1, 1],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0]
    ]

    result = BFS(maze, (5, 5)).solve_maze_bfs(maze)
    if result:
        print("Final Maze:")
        for row in result:
            print(row)
    else:
        print("Không có đường đi từ điểm đầu đến điểm cuối trong maze.")
