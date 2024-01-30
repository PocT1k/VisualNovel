import pygame

from load import *
from scenes import *
from structs import *


def run():
    pygame.init()
    window = createWindow()
    data = loading(window)

    white = (255, 255, 255)
    font = pygame.font.Font(None, 36)
    text = font.render("Начать", True, white)
    window.blit(text, (200, 300))
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            running = stop(event)

    pygame.quit()
pass

if __name__ == '__main__':
    run()
