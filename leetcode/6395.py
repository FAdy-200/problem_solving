# https://leetcode.com/contest/biweekly-contest-105/problems/buy-two-chocolates/
from typing import List
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if sum(prices[:2]) > money:
            return money
        else:
            return money - sum(prices[:2])