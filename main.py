import pygame

from load import *


def run():
    loadingMenu()
    pygame.init()
    # Ожидаем закрытия окна
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
pass

# if __name__ == '__main__':
#     run()