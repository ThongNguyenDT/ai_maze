import pygame

from pygame_gui import UIManager

pygame.init()

test_surface = pygame.display.set_mode((800, 600), 0, 32)
test_surface.fill(pygame.Color(128, 128, 128, 255))

manager = UIManager((800, 600))

options_list = [f"option {x}" for x in range(3)]


running = True
time = 0.0
while running:
    test_surface.fill(pygame.Color(128, 128, 128, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        manager.process_events(event)

    manager.update(0.001)
    time += 0.001
    manager.draw_ui(test_surface)
    pygame.display.update()