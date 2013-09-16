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
                       ball.get_diameter() / 2)
    ball_center = ball.get_center()
    txt_position = (ball_center[0] - ball.get_diameter() / 2.50,
                    ball_center[1] - ball.get_diameter() / 7.75)
    txt_surface = ball.get_txt_font().render(
        ball.get_operation().get_text(), color=ball.get_txt_color())
    surface.blit(txt_surface, txt_position)
