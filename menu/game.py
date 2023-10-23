import pygame
from Algorithm.BFSsolve import bfs
from Algorithm.dfsMapGeneration import DFSMAPGen
from config.config import WHITE, BLACK
from object.draw.UIElement import UIElement
from object.draw.button import Button
from object.gameplay.Cell import Cell


class game:
    def __init__(self, screen, config):
        self.screen = screen
        self.config = config
        self.clock = pygame.time.Clock()
        self.running = False
        # self.previous_choice = ""
        self.start_autoplay = False
        self.path = []
        self.start_game = False
        # self.start_timer = False
        # self.elapsed_time = 0
        # # self.high_score = float(self.get_high_scores()[0])
        self.size = int(self.config.width // self.config.cellsize), int(self.config.heigh // self.config.cellsize)
        self.config.cellsize = self.config.cellsize_ratio(0.75)
        self.grid_cells = [Cell(col, row, map_size=self.size, config=self.config) for row in range(self.size[1]) for col
                           in
                           range(self.size[0])]
        self.current_cell = self.grid_cells[0]
        self.complete_cell = self.grid_cells[-1]
        self.colors, self.color = [], 40
        self.map = DFSMAPGen(self.grid_cells, self.config)
        # cols, rows = self.size

    # def get_high_scores(self):
    #     with open("high_score.txt", "r") as file:
    #         scores = file.read().splitlines()
    #     return scores

    # def save_score(self):
    #     with open("high_score.txt", "w") as file:
    #         file.write(str("%.3f\n" % self.high_score))
    #
    # def time(self):
    #     pass

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        pygame.display.set_caption('MAZE - game')
        # self.elapsed_time = 0
        # self.start_timer = False
        self.start_game = False
        self.start_autoplay = False
        self.directions = {'a': 'left', 'd': 'right', 'w': 'top', 's': 'bottom'}
        self.keys = {'a': pygame.K_a, 'd': pygame.K_d, 'w': pygame.K_w, 's': pygame.K_s}
        self.buttons_list = []
        x, y = self.size[0] * self.config.cellsize + 60, self.size[0] * self.config.cellsize
        self.buttons_list.append(Button(x, y * 0.2, 100, 25, "BFS", WHITE, BLACK, size=15))
        # self.buttons_list.append(Button(500, 170, 200, 50, "Reset", WHITE, BLACK))
        # self.buttons_list.append(Button(425, 450, 100, 50, "BFS", WHITE, BLACK))
        # self.buttons_list.append(Button(550, 450, 100, 50, "DFS", WHITE, BLACK))
        # self.buttons_list.append(Button(675, 450, 100, 50, "UCS", WHITE, BLACK))
        # self.buttons_list.append(Button(300, 450, 100, 50, "Astar", WHITE, BLACK))
        self.path = []
        self.draw()
        self.create_map()
        self.reset_visited()

    def create_map(self):
        isBreak = False
        while not isBreak:
            [cell.draw(self.screen) for cell in self.grid_cells]
            self.current_cell, isBreak = self.map.draw_maze(self.screen, self.current_cell, isBreak)
            self.clock.tick(self.config.fps)
            pygame.display.update()

    def reset_visited(self):
        for cell in self.grid_cells:
            cell.visited = False

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(self.config.fps)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
        # if self.start_game:
        #     if self.current_cell == self.grid_cells[-1]:
        #         self.start_game = False
        #         if self.high_score > 0:
        #             self.high_score = self.elapsed_time if self.elapsed_time < self.high_score else self.high_score
        #         else:
        #             self.high_score = self.elapsed_time
        #         self.save_score()
        #
        #     if self.start_timer:
        #         self.timer = time.time()
        #         self.start_timer = False
        #     self.elapsed_time = time.time() - self.timer
        #
        # if self.start_shuffle:
        #     self.shuffle()
        #     self.draw_tiles()
        #     self.shuffle_time += 1
        #     if self.shuffle_time > 120:
        #         self.start_shuffle = False
        #         self.start_game = True
        #         self.start_timer = True

        if self.start_autoplay:
            if self.autoplay():
                self.start_autoplay = False

    def draw(self):
        self.all_sprites.draw(self.screen)
        self.screen.fill(pygame.Color(self.config.maincolor))
        self.draw_grid()
        self.current_cell.draw_current_cell(self.screen)
        for button in self.buttons_list:
            button.draw(self.screen)
        UIElement(self.size[0] * self.config.cellsize + 60, self.size[0] * self.config.cellsize * 0.08, 'MAZE').draw(
            self.screen)
        if len(self.path) > 0:
            self.current_cell = self.complete_cell
            for i in self.path:
                self.colors.append((min(self.color, 255), 10, 100))
                self.color += 1
            [pygame.draw.rect(self.screen, self.colors[i],
                              (cell.x * self.config.cellsize + 5, cell.y * self.config.cellsize + 5,
                               self.config.cellsize - 10, self.config.cellsize - 10),
                              border_radius=8) for i, cell in enumerate(self.path)]

        # UIElement(550, 35, "%.3f" % self.elapsed_time).draw(self.screen)
        # UIElement(430, 300, "High Score - %.3f" % (self.high_score if self.high_score > 0 else 0)).draw(self.screen)
        pygame.display.flip()

    def draw_grid(self):
        [cell.draw(self.screen) for cell in self.grid_cells]
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            keyup = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                pressed_key = pygame.key.get_pressed()
                for key, key_value in self.keys.items():
                    if pressed_key[key_value] and keyup:
                        keyup = False
                        if self.directions[key] in self.current_cell.possible_move(self.grid_cells):
                            self.current_cell = self.current_cell.possible_move(self.grid_cells)[self.directions[key]]
            if event.type == pygame.KEYUP:
                keyup = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for button in self.buttons_list:
                    if button.click(mouse_x, mouse_y):
                        if button.text == "BFS":
                            self.start_autoplay = True
        #                 if button.text == "Reset":
        #                     self.new()
        #                 if button.text == "BFS":
        #                     self.autoplay(0)
        #                     self.start_autoplay = True
        #                 if button.text == "DFS":
        #                     self.autoplay(1)
        #                     self.start_autoplay = True
        #                 if button.text == "UCS":
        #                     self.autoplay(2)
        #                     self.start_autoplay = True
        #                 if button.text == "Astar":
        #                     self.autoplay(3)
        #                     self.start_autoplay = True

    def autoplay(self):
        self.start_autoplay = False
        self.path = bfs(self.grid_cells, self.current_cell, self.complete_cell, self.screen, self.config)


    def main(self):
        self.screen.fill(pygame.Color(self.config.maincolor))
        self.running = True
        while self.running:
            # UIElement(cols * self.config.cellsize + 60, rows * self.config.cellsize * 0.08,'MAZE').draw(self.screen)

            self.new()
            self.run()
            self.clock.tick(self.config.fps)
            pygame.display.update()
