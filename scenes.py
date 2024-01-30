import pygame


def stop(event): #False = stop
    if event.type == pygame.QUIT:
        return False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            return False
    return True
pass