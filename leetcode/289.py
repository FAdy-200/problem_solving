# https://leetcode.com/problems/game-of-life/
from typing import *
from copy import deepcopy


class Solution:
    def __init__(self):
        self.state_0 = None

    def numberOfNeighbours(self, i, j):
        ans = 0
        for m in range(-1,2,1):
            for n in range(-1,2,1):
                if m == 0 and n == 0:
                    continue
                temp = 0
                if len(self.state_0) > i+m >= 0 and len(self.state_0[0]) > j+n >= 0:
                    temp = self.state_0[i+m][j+n]
                ans += temp
        return ans

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.state_0 = deepcopy(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                n = self.numberOfNeighbours(i, j)
                if board[i][j]:
                    if n < 2:
                        board[i][j] = 0
                    elif n > 3:
                        board[i][j] = 0
                else:
                    if n == 3:
                        board[i][j] = 1


S = Solution()
S.gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])
