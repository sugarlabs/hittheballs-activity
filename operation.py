# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:02:52 2013

@author: laurent-bernabe
"""

OPER_ADD = {'txt': '+', 'operation': lambda op1, op2: op1 + op2}
OPER_SUB = {'txt': '-', 'operation': lambda op1, op2: op1 - op2}
OPER_MUL = {'txt': '*', 'operation': lambda op1, op2: op1 * op2}
OPER_DIV = {'txt': '/', 'operation': lambda op1, op2: op1 / op2}


class Operation(object):

    """
    An abstraction of an operation.
    """

    def __init__(self, op1, op2, operator):
        """
        Constructor
        op1 : numeric value => operand 1
        op2 : numeric value => operand 2
        operator : operator => One of given OPER_* values
                               (for example OPER_ADD)
        """
        self._result = operator['operation'](op1, op2)
        self._txt = str(op1) + operator['txt'] + str(op2)

    def get_result(self):
        """
        Accessor to the result field.
        => numeric value.
        """
        return self._result

    def get_text(self):
        """
        Accessor to the text field
        => string value
        """
        return self._txt
