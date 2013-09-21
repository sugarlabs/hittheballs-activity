# -*- coding: utf-8 -*-
"""
Manages the result bar : this bar that tells to the user which result
he must solve.
Created on Sat Sep 21 11:34:15 2013

@author: laurent-bernabe
"""


class ResultBar(object):

    """
    A bar which tells to the player which result he must solve by hitting
    matching balls.
    """

    def __init__(self, txt_font, txt_color, bg_color, header, width,
                 lftp_edge=(0, 0)):
        """
        Constructor:
        Height will be computed internally thanks to the header value and the
        given font.
        txt_font : text font => olpcgames.pangofont
        txt_color : text color => Tuple of 3 integers in [0,255]
        bg_color : background color => Tuple of 3 integers in [0,255]
        header : text start, such as 'Hit balls with result : ' => string
        width : width of the bar => integer
        lftp_edge : coordinates of the left-top edge => tuple of 2 integers.
        """
        self._INSETS = 4
        self._txt_font = txt_font
        self._txt_color = txt_color
        self._bg_color = bg_color
        self._header = header
        self._width = width
        self._lftp_edge = lftp_edge
        self._height = txt_font.size(header)[1] + 2 * self._INSETS

    def get_insets(self):
        """
        Accessor to the component insets.
        => integer
        """
        return self._INSETS

    def get_text_font(self):
        """
        Accesssor to the text font.
        => olpcgames.pangofont
        """
        return self._txt_font

    def get_foreground(self):
        """
        Accessor to the text color.
        => Tuple of 3 integers in [0,255].
        """
        return self._txt_color

    def get_background(self):
        """
        Accessor to the bar background color.
        => Tuple of 3 integers in [0,255].
        """
        return self._bg_color

    def get_header(self):
        """
        Accessor to the header (text start, such as 'Hit balls with result : ')
        => string
        """
        return self._header

    def get_width(self):
        """
        Accessor to the width.
        => integer
        """
        return self._width

    def get_height(self):
        """
        Accesssor to the height.
        => integer
        """
        return self._height

    def get_edge(self):
        """
        Accessor to the coordinates of the left-top edge.
        => Tuple of 2 integers.
        """
        return self._lftp_edge

    def get_result(self):
        """
        Accessor to the result.
        Careful ! This might throw an NameError, as result may not be defined
        yet.
        => integer
        """
        try:
            return self._result
        except AttributeError:
            raise NameError

    def set_result(self, result):
        """
        Sets the result of the bar.
        result : the result to solve => integer
        """
        self._result = result

    def remove_result(self):
        """
        Delete the result value.
        """
        try:
            del self._result
        except AttributeError:
            pass
