import pygame

from config.config import WHITE


class UIElement:
    def __init__(self, x, y, text):
        self.x, self.y = x, y
        self.text = text
        self.size = 30

    def draw(self, screen, size=None, font=None, color=WHITE):
        if size is None:
            size = self.size
        if font is None:
            font = pygame.font.SysFont("Consolas", size)

        text = font.render(self.text, True, color)
        screen.blit(text, (self.x, self.y))
    def click(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height
