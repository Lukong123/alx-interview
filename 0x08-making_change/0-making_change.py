#!/usr/bin/python3
""" determining the fewest number of coins to be given as change"""

def makeChange(coins, total):
    '''Return: fewest number of coins needed'''
    if total <= 0:
        return 0
    coins.sort()
    coins.reverse()
    change = 0
    for coin in coins:
        if total <= 0:
            break
        tmp = total // coin
        change += tmp
        total -= (tmp * coin)
    if total != 0:
        return -1
    return change
