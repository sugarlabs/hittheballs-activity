# -*- coding: utf-8 -*-
"""
Generates balls.
Created on Mon Sep 23 18:44:00 2013

@author: laurent-bernabe
"""

from random import randint
from ball import Ball
from operation import Operation, OPER_ADD, OPER_SUB, OPER_MUL, OPER_DIV


class OperationConfig(object):

    """
    Stores configuration about a type of operation (OPER_ADD for example) :
    what is the limit for its operands ?
    """

    def __init__(self, op_type, fst_op, snd_op):
        """
        Constructor:
        op_type : operation type => either OPER_ADD, OPER_SUB, OPER_MUL or OPER_DIV
        fst_op : limit, in digit numbers, for first operand => integer
        snd_op : limit, in digit numbers, for second operand => integer
        """
        if op_type == OPER_SUB or op_type == OPER_DIV:
            # First operand can't have less digits than second operand in such
            # cases.
            if fst_op < snd_op:
                raise ValueError("fst_op(%d) can't be less than snd_op(%d)" %
                                 (fst_op, snd_op))
        if fst_op <= 0 or snd_op <= 0:
            raise ValueError(
                "fst_op(%d) and snd_op(%d) must be greater than O." %
                (fst_op, snd_op))
        self._op_type = op_type
        self._fst_op = fst_op
        self._snd_op = snd_op

    def get_operation_type(self):
        """
        Accessor to the operation type.
        => either OPER_ADD, OPER_SUB, OPER_MUL or OPER_DIV
        """
        return self._op_type

    def get_first_operand_limit(self):
        """
        Accessor to the limit, in digits, of the first operand
        => integer
        """
        return self._fst_op

    def get_second_operand_limit(self):
        """
        Accessor to the limit, in digits, of the second operand
        => integer
        """
        return self._snd_op


class BallsGenerator(object):

    """
    Generates a list of balls
    """

    def generate_list(self, balls_number, oper_configs, move_area,
                      txt_font, txt_color):
        """
        Generates a list of Ball instances.
        Firstly, notice that it is not necessary to pass all four operations.
        In such cases only configured operations type will be used for generation.
        Secondly, notice that if you pass several configurations for a same
        operation, only the first configuration matching this operation will be
        used.
        balls_number : number of balls to build => integer
        oper_configs : configurations for the wanted operations => list of
        OperationConfig.
        move_area : space where balls are allowed to be => Tuple of 4 integers (
              left side x, top side y, right side x, bottom side y)
        txt_font : font common to all balls => olpcgames.pangofont
        txt_color : color common to all balls text => tuple of 3 integers between
                  [0,255]
        """
        # We take only one configuration for a given kind of operation.
        filtered_oper_configs = []
        registered_operations = set()
        for config in oper_configs:
            if not config.get_operation_type()["txt"] in registered_operations:
                filtered_oper_configs.append(config)
                registered_operations.add(config.get_operation_type()["txt"])
        # Then we generates balls
        balls = []
        op_type, fst_operand, snd_operand = None, None, None
        for counter in range(balls_number):
            while True:
                op_type_index = randint(1, len(filtered_oper_configs)) - 1
                operation_config = filtered_oper_configs[op_type_index]
                op_type = operation_config.get_operation_type()
                lim_1 = operation_config.get_first_operand_limit()
                lim_2 = operation_config.get_second_operand_limit()
                fst_operand = randint(2, 10 ** lim_1 - 1)
                snd_operand = randint(2, 10 ** lim_2 - 1)
                if op_type == OPER_ADD or op_type == OPER_MUL:
                    break
                elif op_type == OPER_SUB:
                    if fst_operand > snd_operand:
                        break
                elif op_type == OPER_DIV:
                    if fst_operand % snd_operand == 0:
                        break
                else:
                    raise Exception("Unkown operation type")
            ball_bg_color = self._generate_color()
            ball_velocity = self._generate_velocity()
            balls.append(Ball(txt_font, txt_color, ball_bg_color,
                              Operation(fst_operand, snd_operand, op_type),
                              move_area, ball_velocity))
        return balls

    def _generate_color(self):
        """
        Generates a color
        => Tuple of 3 integers between [10, 245[
        """
        red = randint(10, 245)
        green = randint(10, 245)
        blue = randint(10, 245)
        return (red, green, blue)

    def _generate_velocity(self):
        """
        Generates ball velocity
        => Tuple of 2 integers.
        """
        while True:
            x = (200 - randint(0, 400)) / 100  # between -2.0 and 2.0
            y = (200 - randint(0, 400)) / 100  # between -2.0 and 2.0
            velocity = (x, y)
            if abs(velocity[0]) >= 0.5 and abs(velocity[1]) >= 0.5:
                break
        return velocity
