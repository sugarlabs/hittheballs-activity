# -*- coding: utf-8 -*-
"""
Entry point of the application.
Created on Sat Sep 14 10:57:17 2013

@author: laurent-bernabe
"""

from operation import OPER_ADD, OPER_SUB, OPER_MUL, OPER_DIV
from balls_generator import OperationConfig
from main_game import play_game


class Game():

    def __init__(self):
        pass

    def run(self):
        levels = [
            # level 1
            [OperationConfig(OPER_ADD, 9, 9),
             OperationConfig(OPER_MUL, 9, 9),
             OperationConfig(OPER_SUB, 18, 9),
             OperationConfig(OPER_DIV, 81, 9, 9)],
            # level 2
            [OperationConfig(OPER_ADD, 99, 99, 100),
             OperationConfig(OPER_MUL, 99, 9),
             OperationConfig(OPER_SUB, 100, 98),
             OperationConfig(OPER_DIV, 891, 9, 99)],
            # level 3
            [OperationConfig(OPER_ADD, 999, 999, 1000),
             OperationConfig(OPER_MUL, 99, 99, 1000),
             OperationConfig(OPER_SUB, 1000, 998),
             OperationConfig(OPER_DIV, 1000, 99, 99)]
        ]

        play_game(30, levels[2])

if __name__ == "__main__":
    g = Game()
    g.run()
