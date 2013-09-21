# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 10:57:17 2013

@author: laurent-bernabe
"""

import olpcgames
import pygame
from sys import exit
from olpcgames.pangofont import PangoFont
from pygame.locals import QUIT, USEREVENT, MOUSEBUTTONUP
from ball import Ball
from operation import Operation, OPER_ADD, OPER_SUB, OPER_MUL, OPER_DIV
from elements_painter import paint_ball, paint_time_bar, paint_result_bar,\
    paint_results
from time_bar import TimeBar
from result_bar import ResultBar
from game_state import GameState
import balls_collision


def get_result_at_pos(point, balls_list):
    """
    Returns the result of the ball located at point (from the balls_list)
    and its index in the balls_list,
    if any, else returns None.
    point : point to test => tuple of 2 integers
    balls_list : list of balls to test => list of Ball
    => dictionnary with "result" key => value : integer
                         "index" key => value : integer
    """
    for ball_index in range(len(balls_list)):
        ball = balls_list[ball_index]
        if ball.contains(point):
            return {"result": ball.get_operation().get_result(),
                    "index": ball_index}
    return None


def all_target_balls_destroyed(target_result, balls_list):
    """
    Says whether all target ball, those with the expected result, have been
    removed from the given list.
    target_result : expected result => integer
    balls_list : list of balls => list of Ball
    => Boolean
    """
    for ball in balls_list:
        if ball.is_visible() \
                and ball.get_operation().get_result() == target_result:
            return False
    return True


def main():
    """ The main routine """
    pygame.init()
    LEFT_BUTTON = 1
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
    BROWN = (160, 100, 0)

    if olpcgames.ACTIVITY:
        size = olpcgames.ACTIVITY.game_size
        screen = pygame.display.set_mode(size)
    else:
        size = (600, 400)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Hit the balls")
    clock = pygame.time.Clock()
    font = PangoFont(family='Helvetica', size=16, bold=True)
    end_font = PangoFont(family='Helvetica', size=30, bold=True)
    END_TXT_POS = (int(size[0] / 4)), int(size[1] / 2.6)

    game_state = GameState.NORMAL
    target_result = 360

    result_bar = ResultBar(font, txt_color=YELLOW, bg_color=RED,
                           header="Hit the balls with result : ",
                           width=size[0])
    RESULT_BAR_HEIGHT = result_bar.get_height()
    result_bar.set_result(target_result)

    time_bar = TimeBar(size[0], TIME_BAR_HEIGHT, DARK_GREEN, GRAY,
                       lftp_edge=(0, RESULT_BAR_HEIGHT))
    time_bar.start(1000, 1)

    balls_area = (0, TIME_BAR_HEIGHT + RESULT_BAR_HEIGHT, size[0], size[1])

    the_balls = [Ball(font, txt_color=BLACK, bg_color=BLUE,
                      operation=Operation(1000, 3000, OPER_MUL),
                      move_area=balls_area, velocity=(2, 1.2)),
                 Ball(font, txt_color = BLACK, bg_color = YELLOW,
                      operation = Operation(120, 45, OPER_SUB),
                      move_area = balls_area, velocity = (1.6, -0.4)),
                 Ball(font, txt_color = BLACK, bg_color = BROWN,
                      operation = Operation(3, 120, OPER_MUL),
                      move_area = balls_area, velocity = (0.7, -1.8)),
                 Ball(font, txt_color = BLACK, bg_color = RED,
                      operation = Operation(9, 3, OPER_DIV),
                      move_area = balls_area, velocity = (-0.8, 1.6)),
                 Ball(font, txt_color = BLACK, bg_color = GREEN,
                      operation = Operation(120, 240, OPER_ADD),
                      move_area = balls_area, velocity = (1.7, -1.2))]

    balls_collision.place_balls(the_balls, balls_area)

    while True:
        pygame.display.update()
        screen.fill(BACKGROUND)
        paint_result_bar(result_bar, screen)
        paint_time_bar(time_bar, screen)
        if game_state == GameState.NORMAL:
            for ball in the_balls:
                paint_ball(ball, screen)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == USEREVENT + 1:
                    time_bar.decrease()
                    if time_bar.is_empty():
                        result_bar.remove_result()
                elif event.type == MOUSEBUTTONUP:
                    if event.button == LEFT_BUTTON:
                        event_pos = event.pos
                        clicked_ball = get_result_at_pos(event_pos, the_balls)
                        if clicked_ball is not None:
                            if clicked_ball["result"] == target_result:
                                the_balls[clicked_ball["index"]].hide()
                                if all_target_balls_destroyed(
                                        target_result, the_balls):
                                    game_state = GameState.WON
                                    show_status = True
                                    pygame.time.set_timer(USEREVENT + 2, 800)
                            else:
                                game_state = GameState.LOST
                                show_status = True
                                pygame.time.set_timer(USEREVENT + 2, 800)
            clock.tick(FPS)
            for ball in the_balls:
                ball.move()
            balls_collision.manage_colliding_balls(the_balls)
        else:
            paint_results(balls_area, the_balls, screen)
            # Blinks the status text.
            if show_status:
                if game_state == GameState.WON:
                    end_txt = "Success !"
                else:
                    end_txt = "Failure !"
                end_txt_surface = end_font.render(end_txt,
                                                  color=BLUE, background=RED)
                screen.blit(end_txt_surface, END_TXT_POS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == USEREVENT + 2:
                    show_status = not show_status

if __name__ == "__main__":
    main()
