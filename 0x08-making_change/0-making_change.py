#!/usr/bin/python3
"""
Calculates the minimum number of coins needed to make a given amount.

Args:
    coins: A list of coin denominations, sorted in descending order.
    total: The target amount to be made.

Returns:
    Minimum number of coins needed, or -1 if target amount cannot be made.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    coins.sort(reverse=True)
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
