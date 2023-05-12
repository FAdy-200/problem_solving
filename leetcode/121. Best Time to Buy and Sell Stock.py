# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import *


def max_profit(p: List[int]) -> int:
    ma = 0
    abma = 0
    sell = len(p)-1
    absell = sell
    buy = sell-1
    while buy >= 0:
        if p[buy] > p[sell]:
            sell = buy
            buy -= 1
        else:
            ma = p[sell]-p[buy]
            abma = max(abma, p[absell] - p[buy])
            if ma > abma:
                abma = ma
                absell = sell
            buy-=1
    return abma


prices = [7,1,5,3,6,4]
x = [1,2]
print(max_profit(x))
