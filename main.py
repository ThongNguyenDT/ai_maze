import pygame

from config.logicConfig import Config
from menu.game import game
from menu.menu import main_menu

config = Config()
config.config_load()

RES = config.width, config.heigh

pygame.init()
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()


click = False
main = game(sc, config).main


def options():
    pass


while True:
    sc.fill(pygame.Color(config.maincolor))
    click = main_menu(sc, click=click, callbacks=[main, options])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    pygame.display.flip()
    clock.tick(config.fps)
