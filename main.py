# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 10:57:17 2013

@author: laurent-bernabe
"""

import olpcgames
import pygame
from sys import exit
from olpcgames.pangofont import PangoFont
from pygame.locals import QUIT, USEREVENT
from ball import Ball
from operation import Operation, OPER_ADD, OPER_SUB, OPER_MUL, OPER_DIV
from elements_painter import paint_ball, paint_time_bar
from time_bar import TimeBar
import balls_collision


def main():
    """ The main routine """
    pygame.init()
    FPS = 40
    BACKGROUND = (255, 255, 255)
    TIME_BAR_HEIGHT = 20
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    DARK_GREEN = (0, 100, 0)
    GRAY = (200, 200, 200)    
    if olpcgames.ACTIVITY:
        size = olpcgames.ACTIVITY.game_size
        screen = pygame.display.set_mode(size)
    else:
        size = (600, 400)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Hit the balls")
    clock = pygame.time.Clock()
    font = PangoFont(family='Helvetica', size=16, bold=True)
    
    time_bar = TimeBar(size[0], TIME_BAR_HEIGHT, DARK_GREEN, GRAY)
    time_bar.start(1000, 1)
    
    balls_area = (0, TIME_BAR_HEIGHT, size[0], size[1])
    
    the_balls = [Ball(font, BLACK, BLUE, 
                      Operation(1000, 3000, OPER_MUL), balls_area, (2, 1.2)),
                 Ball(font, BLACK, YELLOW, 
                      Operation(120, 45, OPER_SUB), balls_area, (1.6,-0.4)),
                 Ball(font, BLACK, RED, 
                      Operation(9, 3, OPER_DIV), balls_area, (-0.8, 1.6)),
                 Ball(font, BLACK, GREEN,
                      Operation(120, 240, OPER_ADD), balls_area, (1.7, -1.2))]
                

    balls_collision.place_balls(the_balls, balls_area)
    
    while True:
        screen.fill(BACKGROUND)
        paint_time_bar(time_bar, screen)
        for ball in the_balls:
            paint_ball(ball, screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == USEREVENT + 1:
                time_bar.decrease()
        pygame.display.update()
        clock.tick(FPS)
        for ball in the_balls:
            ball.move()
        balls_collision.manage_colliding_balls(the_balls)

if __name__ == "__main__":
    main()
