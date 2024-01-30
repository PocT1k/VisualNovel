import pygame

from load import *
from scenes import *
from structs import *


def run():
    pygame.init()
    window = createWindow()
    data = loading(window)

    running = True
    while running:
        for event in pygame.event.get():
            running = stop(event)

    pygame.quit()
pass

if __name__ == '__main__':
    run()
