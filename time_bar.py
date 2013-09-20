# -*- coding: utf-8 -*-
"""
Manages time bar : a kind of reversed progress bar.
Created on Fri Sep 20 23:19:47 2013

@author: laurent-bernabe
"""

import pygame
from pygame.locals import USEREVENT

class TimeBar(object):
    """
    A kind of reversed progress bar.
    """
    
    def __init__(self, width, height, active_color, dead_color, 
                 lftp_edge=(0,0)):
        """
        Constructor
        width : width of the bar (when it has its maximum value) => integer
        height : height of the bar => integer
        active_color : color for active part => Tuple of 3 integers in [0,255]
        dead_color : color for the dead part => Tuple of 3 integers in [0,255]
        lftp_edge : coordinate of the left-top edge => tuple of two integers
        """
        self._width = width
        self._height = height
        self._lftp_edge = lftp_edge
        self._active_color = active_color
        self._dead_color = dead_color
        
    def start(self, max_value, step):
        """
        Starts a new 'session'. Please, notice that time between two stages
        (or ticks) is 100 milliseconds, and that you must call decrease()
        method on USEREVENT+1 event of pygame.
        max_value : the start value (don't forget that it is a reversed
        progress bar) => integer
        step : how many units will be removed at each stage => integer
        """
        self._value = max_value
        self._max_value = max_value
        self._step = step
        pygame.time.set_timer(USEREVENT + 1, 100)

    def decrease(self):
        """
        Decreases the value of the time bar, and stops its falling if there
        is no more value unit.
        """
        self._value -= self._step
        if self._value <= 0:
            pygame.time.set_timer(USEREVENT + 1, 0)
    
    def get_width(self):
        """
        Accessor to the width (width when it has its maximum value)
        => integer
        """
        return self._width
        
    def get_height(self):
        """
        Accessor to the height
        => integer
        """
        return self._height
        
    def get_edge(self):
        """
        Accessor to the left-top edge.
        => tuple of two integers
        """
        return self._lftp_edge
        
    def get_active_color(self):
        """
        Accessor to the active part (not elapsed) color.
        => Tuple of 3 integers.
        """
        return self._active_color
        
    def get_dead_color(self):
        """
        Accessor to the dead part (elapsed) color.
        => Tuple of 3 integers
        """
        return self._dead_color
        
    def get_value(self):
        """
        Accessor to the value.
        Be careful ! May raise NameError, as value may not be defined yet.
        => integer
        """
        try:
            return self._value
        except AttributeError:
            raise NameError
        
    def get_max_value(self):
        """
        Accessor to the max value.
        Be careful ! May raise NameError, as max value may not be defined yet.
        => integer
        """
        try:
            return self._max_value
        except AttributeError:
            raise NameError