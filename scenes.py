import pygame


def stopRun(event): #False = stop
    if event.type == pygame.QUIT:
        return False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            return False
    return True
pass

def showMenu(data):
    data['menu']['background'].show()
    data['menu']['buttomDarkBrown'].show()
    data['menu']['textStart'].show()
    data['menu']['logoODINart'].show(0.15, 0.9)
    pygame.display.update()
pass

def runMenu(window, data):
    showMenu(data)
    rect = data['menu']['buttomLightBrown'].rect

    running = True
    while running:
        for event in pygame.event.get():
            running = stopRun(event)
            if event.type == pygame.MOUSEMOTION:
                if rect.collidepoint(event.pos): #pygame.mouse.get_pos()
                    data['menu']['buttomLightBrown'].show()
                    pygame.display.update()
                else:
                    pygame.display.update()
pass
