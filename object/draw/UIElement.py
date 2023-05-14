import pygame

from config.config import WHITE


class UIElement:
    def __init__(self, x, y, text):
        self.x, self.y = x, y
        self.text = text

    def draw(self, screen, color=WHITE):
        font = pygame.font.SysFont("Consolas", 30)
        text = font.render(self.text, True, color)
        screen.blit(text, (self.x, self.y))