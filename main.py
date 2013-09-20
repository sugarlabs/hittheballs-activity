# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 10:57:17 2013

@author: laurent-bernabe
"""

import olpcgames
import pygame
from sys import exit
from olpcgames.pangofont import PangoFont
from pygame.locals import QUIT
from ball import *
from operation import *
from elements_painter import *


def main():
    """ The main routine """
    pygame.init()
    FPS = 40
    BACKGROUND = (255, 255, 255)
    if olpcgames.ACTIVITY:
        size = olpcgames.ACTIVITY.game_size
        screen = pygame.display.set_mode(size)
    else:
        size = (600, 400)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Hit the balls")
    clock = pygame.time.Clock()
    font = PangoFont(family='Helvetica', size=16, bold=True)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    the_ball = Ball(font, BLACK, BLUE, Operation(1000, 3000, OPER_MUL),
                    (2, 1.2))
    the_ball.move_to((140, 170))
    
    while True:
        screen.fill(BACKGROUND)
        paint_ball(the_ball, screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(FPS)
        the_ball.move()

if __name__ == "__main__":
    main()
