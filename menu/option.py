import sys

import pygame

from config.config import WHITE, BLACK
from config.logicConfig import Config
from menu.game import game
from menu.setting import screens, levels
from object.draw.UIElement import UIElement
from object.draw.button import Button


class option:
    def __init__(self, screen, config, manager, callback):
        self.screen = screen
        self.config = config
        self.manager = manager
        self.clock = pygame.time.Clock()
        self.buttons_list = []
        self.center_x, self.center_y = self.config.width / 2, self.config.height / 2
        self.callback = callback

    def main(self):
        self.screen.fill(pygame.Color(self.config.maincolor))
        self.running = True
        while self.running:
            self.new()
            self.uinew()
            self.run()

    def new(self):
        self.width, self.height, self.selected_level = self.config.width, self.config.height, self.config.level
        self.buttons_list = []
        self.center_x, self.center_y = self.config.width / 2, self.config.height / 2
        self.buttons_list.append(
            Button(self.center_x, self.config.height - 100, 200, 50, 'game', WHITE, BLACK, size=20, center=True))
        self.buttons_list.append(
            Button(self.center_x, 100, 200, 50, 'resolution', WHITE, BLACK, size=20, center=True))
        self.buttons_list.append(
            Button(self.center_x, 275, 200, 50, 'level', WHITE, BLACK, size=20, center=True))

        self.res = [str(screeni[0]) + "x" + str(screeni[1]) if type(screeni) is tuple else screeni for screeni in
                    screens]
        self.level = [str(x) for x in levels]

    def run(self):
        self.playing = True
        while self.playing:
            self.screen.fill(pygame.Color(self.config.maincolor))
            self.event()
            self.draw()

    def draw(self):
        for button in self.buttons_list:
            button.draw(self.screen)
        UIElement(self.center_x, 20, 'Option').draw_center_x(self.screen,
                                                             font=pygame.font.Font('assets/font/emulogic.ttf', 30))
        pygame.display.update()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for button in self.buttons_list:
                    if button.click(mouse_x, mouse_y):
                        if button.text == 'game':
                            new_config = Config(width=self.width, height=self.height, level=self.selected_level)
                            game(self.screen, self.config).main()


