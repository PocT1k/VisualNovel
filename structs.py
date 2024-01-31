import pygame

ratioStandard = 16.0 / 9.0
widthStandard = 1920.0
heightStandard = 1080.0


def calculatingSize(windowSize): #Вычисление размеров для масштабирования
    w, h = windowSize[0], windowSize[1]
    ratioWindow = w / h

    if ratioWindow == ratioStandard: #Стандартное соотношение 16 к 9
        return (w, h)
    elif ratioWindow > ratioStandard: #Шире стандарта
        return(h * ratioStandard, h)
    else: #Уже стандарта
        return (w, w / ratioStandard)

    # else:
    #     if h > w: #Уже чем 1 к 1
    #         return (w * ratioStandard, w)
    #     else:
    #         return (w * ratioStandard, h)
pass

def calculatingZeroPoint(windowSize, newSize):
    w, h = 0, 0
    if windowSize[0] > newSize[0]:
        w = (windowSize[0] - newSize[0]) / 2.0
    if windowSize[1] > newSize[1]:
        h = (windowSize[1] - newSize[1]) / 2.0
    return (w, h)
pass

class FullPicture():
    def __init__(self, window, path, picture, ext, alpha = False):
        self.window = window

        if alpha: self.picture = pygame.image.load(path + picture + ext).convert_alpha() # Загрузка
        else: self.picture = pygame.image.load(path + picture + ext)

        self.windowSize = window.get_size()#pygame.display.Info() # Определение размеров
        self.pictureSize = calculatingSize(self.windowSize)
        self.picture = pygame.transform.scale(self.picture, self.pictureSize) # Масштабирование

        self.rect = self.picture.get_rect() # Центрирование
        self.windowRect = window.get_rect()
        self.rect.center = self.windowRect.center
    pass

    def show(self):
        self.window.blit(self.picture, self.rect)
    pass
pass

class PartialPicture():
    def __init__(self, window, path, picture, ext, alpha = False):
        self.window = window

        if alpha: self.picture = pygame.image.load(path + picture + ext).convert_alpha() # Загрузка
        else: self.picture = pygame.image.load(path + picture + ext)

        self.windowSize = window.get_size()#pygame.display.Info() # Определение размеров
        self.pictureSize = calculatingSize(self.windowSize)
        self.rect = self.picture.get_rect()
        self.newSize = (self.rect[2] * self.pictureSize[0] / widthStandard,
                        self.rect[3] * self.pictureSize[1] / heightStandard)
        self.picture = pygame.transform.scale(self.picture, self.newSize) # Масштабирование

        self.zeroPoint = calculatingZeroPoint(self.windowSize, self.pictureSize) # Центрирование
        self.rect = self.picture.get_rect()
        self.windowRect = window.get_rect()
        self.rect.center = self.windowRect.center
    pass

    def show(self, shiftx = 0.5, shifty = 0.5):
        self.rect.centerx = self.zeroPoint[0] + self.pictureSize[0] * shiftx
        self.rect.centery = self.zeroPoint[1] + self.pictureSize[1] * shifty
        self.window.blit(self.picture, self.rect)
    pass
pass

class TextMenu():
    def __init__(self, window, text, alpha = 255):
        self.window = window

        self.windowSize = window.get_size()  # pygame.display.Info() # Определение размеров
        self.pictureSize = calculatingSize(self.windowSize)
        self.fontSize = int(144 * self.pictureSize[0] / widthStandard)

        self.color = (255, 255, 255) # Создание шрифта
        self.font = pygame.font.Font(None, self.fontSize)
        self.text = self.font.render(text, True, self.color)
        self.text.set_alpha(alpha)

        self.zeroPoint = calculatingZeroPoint(self.windowSize, self.pictureSize) # Центрирование
        self.rect = self.text.get_rect()
        self.windowRect = window.get_rect()
        self.rect.center = self.windowRect.center
    pass

    def show(self, shiftx = 0.5, shifty = 0.5):
        self.rect.centerx = self.zeroPoint[0] + self.pictureSize[0] * shiftx
        self.rect.centery = self.zeroPoint[1] + self.pictureSize[1] * shifty
        self.window.blit(self.text, self.rect)
    pass
pass
