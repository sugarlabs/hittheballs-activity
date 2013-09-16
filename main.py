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
    font = PangoFont(family='Helvetica', size=16, bold=True)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    the_balls = [Ball(font, BLACK, BLUE, Operation(1000, 3000, OPER_MUL)),
                 Ball(font, BLACK, YELLOW, Operation(120, 45, OPER_SUB)),
                 Ball(font, BLACK, RED, Operation(9, 3, OPER_DIV)),
                 Ball(font, BLACK, GREEN, Operation(120, 240, OPER_ADD))]
    the_balls[0].move((140, 170))
    the_balls[1].move((400, 300))
    the_balls[2].move((200, 80))
    the_balls[3].move((330, 70))

    while True:
        screen.fill(BACKGROUND)
        for ball in the_balls:
            paint_ball(ball, screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
