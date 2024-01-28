import pygame


def createWindow():
    # window = pygame.display.set_mode((720, 720))
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Новогодний рассказ")
    bg_color = (180, 215, 245)
    window.fill(bg_color)
    pygame.display.update()

    return window
pass

def loading(window):
    data = loadingMenu()
    return data
pass

def loadingMenu():
    path = 'resources/images/menu/'

    data = {
        'menu': {
            'background': pygame.image.load(path + 'background.png')
        }
    }

    return data
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
