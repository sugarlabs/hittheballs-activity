# -*- coding: utf-8 -*-
"""
Manages balls collisions
Created on Fri Sep 20 19:57:22 2013

@author: laurent-bernabe
"""

from math import sqrt

def are_colliding_balls(ball_1, ball_2):
    """
    Says whether two balls collides.
    ball_1 : ball to test => Ball
    ball_2 : ball to test => Ball
    => Boolean
    """
    b1_x, b1_y = ball_1.get_center()
    b2_x, b2_y = ball_2.get_center()
    x_dist = abs(b1_x - b2_x)
    y_dist = abs(b1_y - b2_y)
    b1_radius = ball_1.get_diameter() / 2
    b2_radius = ball_2.get_diameter() / 2
    centers_dist = sqrt(x_dist**2 + y_dist**2)
    return centers_dist <= (b1_radius + b2_radius)
    
def manage_colliding_balls(balls_list):
    """
    Detects all colliding balls couples of balls_list,
    and, for each colliding balls couple, alter both ball
    velocity and make a move for both.
    balls_list : list of balls => List of Ball
    """
    for fst_ball_index in range(len(balls_list[:-1])):
        fst_ball = balls_list[fst_ball_index]        
        inner_range = range(fst_ball_index + 1, len(balls_list))
        for snd_ball_index in inner_range:
            snd_ball = balls_list[snd_ball_index]
            if (are_colliding_balls(fst_ball, snd_ball)):
                fst_ball.oppose_velocity_and_move()
                snd_ball.oppose_velocity_and_move()