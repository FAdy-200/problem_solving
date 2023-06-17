# https://leetcode.com/problems/online-stock-span/description
from USEFUL_CODES.LC import *


class StockSpanner:

    def __init__(self):
        self.days = deque()

    def next(self, price: int) -> int:
        ans = 0
        while ans < len(self.days):
            if self.days[ans][0] <= price:
                ans += self.days[ans][1]
            else:
                break

        self.days.appendleft([price, ans + 1])
        return ans + 1
