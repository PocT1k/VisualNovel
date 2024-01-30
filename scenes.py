import pygame


def controlMenu(window, data):
    data['menu']['background'].show()
    data['menu']['buttomDarkBrown'].show()
    data['menu']['ODINart'].show(0.15, 0.9)
    data['menu']['textMenu'].show()

    pygame.display.update()
pass

def stop(event): #False = stop
    if event.type == pygame.QUIT:
        return False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            return False
    return True
pass
