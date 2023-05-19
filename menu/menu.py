import sys

import pygame

from object.draw.UIElement import UIElement


# def main_menu(screen, click=False, callback={}):
def main_menu(screen, click=False, callbacks=None):
    # draw_text('main menu', font, (255, 255, 255), screen, 20, 20)

    if callbacks is None:
        callbacks = []
    UIElement(20, 20, 'main menu').draw(screen, font=pygame.font.Font('assets/font/emulogic.ttf'))

    mx, my = pygame.mouse.get_pos()
    y = 100
    # for x, func in callback:
    for callback in callbacks:
        button = pygame.Rect(50, y, 200, 50)
        y += 100
        if button.collidepoint((mx, my)):
            if click:
                callback()
        pygame.draw.rect(screen, (255, 0, 0), button)

    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
        return click

