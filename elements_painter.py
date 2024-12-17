# -*- coding: utf-8 -*-

"""
HitTheBalls : hit the ball(s) with the good result.
Copyright (C) 2013  Laurent Bernabe <laurent.bernabe@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

"""
Knows how to paint the elements onto a PyGame Surface.
"""

import pygame


def paint_ball(ball, surface):
    """
    Draws a ball onto the given PyGame surface.
    ball : the ball to draw => Ball instance
    surface : the destination surface => PyGame.Surface
    (returns sequence of Rect, or an empty sequence)
    """
    s = []
    if ball.is_visible():
        r = pygame.draw.circle(surface, ball.get_bg_color(), ball.get_center(),
                               int(ball.get_diameter() / 2))
        s.append(r)

        ball_center = ball.get_center()
        text = ball.get_display_text()
        font = ball.get_txt_font()

        bg_color = ball.get_bg_color()
        brightness = (0.299 * bg_color[0] + 0.587 * bg_color[1] + 0.114 * bg_color[2]) / 255

        if brightness > 0.5:  
            text_color = (0, 0, 0) 
        else:  
            text_color = (255, 255, 255) 

        text_surface = font.render(text, True, text_color)

        surface.blit(text_surface, (ball_center[0] - text_surface.get_width() / 2, ball_center[1] - text_surface.get_height() / 2))
        
        s.append(r)
    return s


def paint_time_bar(time_bar, surface):
    """
    Draws a time bar onto the given PyGame surface.
    time_bar : the time bar => TimeBar
    surface : the destination surface => PyGame.Surface
    (returns sequence of Rect)
    """
    s = []
    edge = time_bar.get_edge()
    dead_rect = (edge[0], edge[1],
                 time_bar.get_width(), time_bar.get_height())
    r = pygame.draw.rect(surface, time_bar.get_dead_color(), dead_rect)
    s.append(r)
    try:
        value = time_bar.get_value()
        max_value = time_bar.get_max_value()
        active_rect = (edge[0], edge[1],
                       int(time_bar.get_width() * value / max_value),
                       time_bar.get_height())
        r = pygame.draw.rect(surface, time_bar.get_active_color(), active_rect)
    except NameError:
        r = pygame.draw.rect(surface, time_bar.get_active_color(), dead_rect)
    s.append(r)
    return s


def paint_result_bar(result_bar, surface):
    """
    Draws a result bar onto a given PyGame surface.
    result_bar : the result bar => ResultBar
    surface : the destination surface => PyGame.Surface
    (returns sequence of Rect)
    """
    s = []
    edge = result_bar.get_edge()
    rect = (edge[0], edge[1],
            result_bar.get_width(), result_bar.get_height())
    r = pygame.draw.rect(surface, result_bar.get_background(), rect)
    s.append(r)
    try:
        text = result_bar.get_header() + str(result_bar.get_result())
    except NameError:
        text = result_bar.get_header()
    text_surface = result_bar.get_text_font().render(
        text, 1, result_bar.get_foreground())
    r = surface.blit(text_surface,
                     (edge[0] + result_bar.get_insets(),
                      edge[1] + result_bar.get_insets()))
    s.append(r)
    return s


def paint_results(game_area, balls_list, surface):
    """
    Draws all results, with their ball color as "header".
    game_area : area of the balls => tuple of 4 integer
    balls_list : list of balls => list of Ball
    surface : the destination surface => PyGame.Surface
    (returns sequence of Rect)
    """
    s = []
    font = pygame.font.Font(None, 40)
    #font = PangoFont(family='Helvetica', size=16)
    LINE_HEIGHT = font.size("0123456789")[1]
    CIRCLES_RADIUS = LINE_HEIGHT // 2
    ball_index = 0
    BLACK = (0, 0, 0)
    for ball in balls_list:
        r = pygame.draw.circle(surface, ball.get_bg_color(),
                          (game_area[0] + CIRCLES_RADIUS,
                           game_area[
                               1] + ball_index * LINE_HEIGHT + CIRCLES_RADIUS),
                           CIRCLES_RADIUS)
        s.append(r)
        txt = ball.get_operation().get_text() + " = " + str(ball.get_operation().
                                                            get_result())
        txt_surface = font.render(txt, 1, BLACK)
        r = surface.blit(txt_surface,
                     (game_area[0] + 40, game_area[1] + ball_index * LINE_HEIGHT))
        s.append(r)
        ball_index += 1
    return s
