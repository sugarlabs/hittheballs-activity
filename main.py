# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 10:57:17 2013

@author: laurent-bernabe
"""

import olpcgames
import pygame
import sys
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
    info = pygame.display.Info()
    screen_size = info.current_w, info.current_h
    font = PangoFont(family='Helvetica', size=30, bold=True)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    the_ball = Ball(font, WHITE, BLUE, Operation(1000, 3000, OPER_MUL))
    the_ball.move((140, 170))
    while True:
        screen.fill(BACKGROUND)
        paint_ball(the_ball, screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
