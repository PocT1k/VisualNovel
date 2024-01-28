import pygame

from load import *


def run():
    pygame.init()
    window = createWindow()
    data = loading(window)

    #window.blit(dataMenu['background'], (0, 0))
    pygame.display.update()

    # Ожидаем закрытия окна
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
pass

if __name__ == '__main__':
    run()
