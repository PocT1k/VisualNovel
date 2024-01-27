import pygame


def loadingMenu():
    path = 'resources/images/menu/'
    menu = {
        'background': pygame.image.load(path + 'background.png')
    }

    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Новогодний рассказ")
    bg_color = (180, 215, 245)
    screen.fill(bg_color)
    screen.blit(menu['background'], (0, 0))
    pygame.display.update()

    pygame.quit()
pass

def loadingResources():
    pass
    # Ресурсы

    # Фоны

    # Сценки

    # Спрайты

    # Персонажи


    # Музыка

    # Звуки

    # Эмбиент


    # Сценарий

pass
