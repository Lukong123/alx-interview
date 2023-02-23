#!/usr/bin/python3
"""minimum operations"""


def minOperations(n):
    '''returns minimum operations'''
    op = 0
    val = 1
    cp = 0
    while (val < n):
        if((n % val) == 0):
            op += 2
            cp = val
            val *= 2
        else:
            op += 1
            val += cp
    return op
