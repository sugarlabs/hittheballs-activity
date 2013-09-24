# -*- coding: utf-8 -*-
"""
Entry point of the application.
Created on Sat Sep 14 10:57:17 2013

@author: laurent-bernabe
"""

from operation import OPER_ADD, OPER_SUB, OPER_MUL, OPER_DIV
from balls_generator import OperationConfig
from main_game import play_game

if __name__ == "__main__":
    operations_config = [OperationConfig(OPER_ADD, 2, 2),
                         OperationConfig(OPER_MUL, 2, 1),
                         OperationConfig(OPER_SUB, 2, 2),
                         OperationConfig(OPER_DIV, 2, 2)]

    play_game(30, operations_config)
