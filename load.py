import pygame

from structs import *
from scenes import *


def createWindow():
    #window = pygame.display.set_mode((1280, 720)) #1920 1080
    window = pygame.display.set_mode((1920, 1080))
    #window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Новогодний рассказ")
    bg_color = (180, 215, 245)
    window.fill(bg_color)
    pygame.display.update()

    return window
pass

def loadImagine(dictionary, window, path, picture, ext, partial=False, alpha=False):
    if partial:
        dictionary[picture] = PartialPicture(window, path, picture, ext, alpha)
    else:
        dictionary[picture] = FullPicture(window, path, picture, ext)
pass

def loadMenu(window, data):
    data['menu'] = dict()
    dictionary = data['menu']
    path = 'resources/images/menu/'

    # Перечисление данных для меню
    fullPictures = [
        'background'
    ]
    partialPictures = [
        'buttomDarkBrown',
        'lightDarkBrown',
        'ODINart'
    ]

    for picture in fullPictures:
        loadImagine(dictionary, window, path, picture, '.png')
    for picture in partialPictures:
        loadImagine(dictionary, window, path, picture, '.png', True)

    dictionary['textMenu'] = TextMenu(window, 'НАЧАТЬ')

    controlMenu(window, data)
pass



def loadAll():
    # Меню mn - грузится отдельно
    # Текст tx - грузится отдельно


    # Ресурсы rs

    # Фоны bg

    # Сценки cg

    # Спрайты sp

    # Персонажи cs


    # sound
    # Музыка mus

    # Звуки sfx

    # Эмбиент amb


    # Сценарий txt
    pass
pass

def loading(window):
    data = dict()
    loadMenu(window, data)
    return data
pass
