import sys

import pygame

from object.draw.UIElement import UIElement


def main_menu(screen, click=False):
    # draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
    UIElement(20, 20, 'main menu').draw(screen, font=pygame.font.Font('../assets/font/emulogic.ttf'))

    mx, my = pygame.mouse.get_pos()

    button_1 = pygame.Rect(50, 100, 200, 50)
    button_2 = pygame.Rect(50, 200, 200, 50)
    if button_1.collidepoint((mx, my)):
        if click:
            pass
    if button_2.collidepoint((mx, my)):
        if click:
            pass
    pygame.draw.rect(screen, (255, 0, 0), button_1)
    pygame.draw.rect(screen, (255, 0, 0), button_2)

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
