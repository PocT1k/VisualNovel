import pygame

ratioStandard = 16.0 / 9.0
widthStandard = 1920
heightStandard = 1080


def calculatingSize(windowSize): #Вычисление размеров для масштабирования
    w, h = windowSize[0], windowSize[1]
    ratioWindow = w / h

    if ratioWindow == ratioStandard: #Стандартное соотношение 16 к 9
        return (w, h)
    elif ratioWindow > ratioStandard: #Шире стандарта
        return(h * ratioStandard, h)

    else: #Уже стандарта
        if h > w: #Уже чем 1 к 1
            return (w * ratioStandard, w)
        else:
            return (w * ratioStandard, h)
pass

def calculatingScale(windowSize):
    pass
pass

class FullPicture():
    def __init__(self, window, path, picture, ext, alpha=False):
        self.window = window

        # Загрузка
        if alpha:
            self.picture = pygame.image.load(path + picture + ext).convert_alpha()
        else:
            self.picture = pygame.image.load(path + picture + ext)
        windowSize = calculatingSize(window.get_size()) #pygame.display.Info()
        self.picture = pygame.transform.scale(self.picture, windowSize)

        # Центрирование
        self.rect = self.picture.get_rect()
        self.windowRect = window.get_rect()
        self.rect.center = self.windowRect.center
    pass

    def show(self):
        self.window.blit(self.picture, self.rect)
pass

class PartialPicture():
    def __init__(self, window, path, picture, ext, alpha=False, shiftx = 50.0, shifty = 50.0):
        self.window = window

        # Загрузка
        if alpha:
            self.picture = pygame.image.load(path + picture + ext).convert_alpha()
        else:
            self.picture = pygame.image.load(path + picture + ext)
        windowSize = calculatingSize(window.get_size()) #pygame.display.Info()
        #self.picture = pygame.transform.scale(self.picture, windowSize)
        # Центрирование
        self.rect = self.picture.get_rect()
        self.windowRect = window.get_rect()
        self.rect.center = self.windowRect.center

    pass

    def show(self):
        self.window.blit(self.picture, self.rect)
pass