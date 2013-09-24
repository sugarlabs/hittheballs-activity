# -*- coding: utf-8 -*-
"""
Manages the main game.
Created on Tue Sep 24 13:54:20 2013

@author: laurent-bernabe
"""

import olpcgames
import pygame
from random import randint
from sys import exit
from olpcgames.pangofont import PangoFont
from pygame.locals import QUIT, USEREVENT, MOUSEBUTTONUP
from elements_painter import paint_ball, paint_time_bar, paint_result_bar,\
    paint_results
from time_bar import TimeBar
from result_bar import ResultBar
from game_state import GameState
from balls_generator import BallsGenerator
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


def play_game(time_seconds, operations_config):
    """ The main game routine
        time_seconds : time limit in seconds => integer
        operations_config : configurations for the wanted operations => list of
        OperationConfig.
    """
    pygame.init()
    LEFT_BUTTON = 1
    FPS = 40
    BACKGROUND = (255, 255, 255)
    TIME_BAR_HEIGHT = 20
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)
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
    end_font = PangoFont(family='Helvetica', size=30, bold=True)
    END_TXT_POS = (int(size[0] / 4)), int(size[1] / 2.6)

    game_state = GameState.NORMAL

    result_bar = ResultBar(font, txt_color=YELLOW, bg_color=RED,
                           header="Hit the ball(s) with result : ",
                           width=size[0])
    RESULT_BAR_HEIGHT = result_bar.get_height()

    time_bar = TimeBar(size[0], TIME_BAR_HEIGHT, DARK_GREEN, GRAY,
                       lftp_edge=(0, RESULT_BAR_HEIGHT))
    # Don't forget that it will take time argument * 10 milliseconds
    time_bar.start(time_seconds * 100, 1)

    balls_area = (0, TIME_BAR_HEIGHT + RESULT_BAR_HEIGHT, size[0], size[1])

    the_balls = BallsGenerator().generate_list(5, operations_config,
                                               balls_area, font, BLACK)

    result_index = randint(1, len(the_balls)) - 1
    target_result = the_balls[result_index].get_operation().get_result()
    result_bar.set_result(target_result)

    balls_collision.place_balls(the_balls, balls_area)
    show_status = True
    pygame.time.set_timer(USEREVENT + 2, 800)

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
                        game_state = GameState.LOST
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
                            else:
                                game_state = GameState.LOST
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
