import pygame

from load import *


def run():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Новогодний рассказ")
    bg_color = (180, 215, 245)
    screen.fill(bg_color)
    screen.blit(menu['background'], (0, 0))
    pygame.display.update()

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