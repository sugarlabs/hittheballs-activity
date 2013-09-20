# -*- coding: utf-8 -*-
"""
Knows how to paint the elements onto a PyGame Surface.

Created on Sun Sep 15 01:28:19 2013

@author: laurent-bernabe
"""

import pygame


def paint_ball(ball, surface):
    """
    Draws a ball onto the given PyGame surface.
    ball : the ball to draw => Ball instance
    surface : the destination surface => PyGame.Surface
    """
    pygame.draw.circle(surface, ball.get_bg_color(), ball.get_center(),
                       int(ball.get_diameter() / 2))
    ball_center = ball.get_center()
    txt_width, txt_height = ball.get_txt_font().size(ball.get_operation().
                                                     get_text())
    txt_position = (int(ball_center[0] - txt_width / 2),
                    int(ball_center[1] - txt_height / 2))
    txt_surface = ball.get_txt_font().render(
        ball.get_operation().get_text(), color=ball.get_txt_color())
    surface.blit(txt_surface, txt_position)
    
def paint_time_bar(time_bar, surface):
    """
    Draws a time bar onto the given PyGame surface.
    time_bar : the time bar => TimeBar
    surface : the destination surface => PyGame.Surface
    """
    edge = time_bar.get_edge()    
    dead_rect = (edge[0], edge[1],
                 time_bar.get_width(), time_bar.get_height())
    pygame.draw.rect(surface, time_bar.get_dead_color(), dead_rect)
    try:
        value = time_bar.get_value()
        max_value = time_bar.get_max_value()
        active_rect = (edge[0], edge[1],
                       int(time_bar.get_width() * value / max_value),
                       time_bar.get_height())
        pygame.draw.rect(surface, time_bar.get_active_color(), active_rect)
    except NameError:
        pygame.draw.rect(surface, time_bar.get_active_color(), dead_rect)
