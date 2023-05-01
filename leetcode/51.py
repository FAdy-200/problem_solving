# https://leetcode.com/problems/n-queens/
from typing import *


class Solution:
    def __init__(self):
        self.n = 0

    def checkAndElemenate(self, i: int, j: int, board: List[List[str]]):
        for m in range(self.n):
            if m != j:  # Horizontal
                board[i][m] = "."
            if m != i:  # Vertical
                board[m][j] = "."

        #  Top half of main diagonal
        ti, tj = i - 1, j - 1
        while ti >= 0 and tj >= 0:
            board[ti][tj] = "."
            ti -= 1
            tj -= 1

        #  Bottom half of main diagonal
        ti, tj = i + 1, j + 1
        while ti < self.n and tj < self.n:
            board[ti][tj] = "."
            ti += 1
            tj += 1

        #  Top half of secondary diagonal
        ti, tj = i - 1, j + 1
        while ti >= 0 and tj < self.n:
            board[ti][tj] = "."
            ti -= 1
            tj += 1

        #  Bottom half of secondary diagonal
        ti, tj = i + 1, j - 1
        while ti < self.n and tj >= 0:
            board[ti][tj] = "."
            ti += 1
            tj -= 1

        # print(board)

    def recursive(self, r: int, board: List[List[str]]) -> List[List[str]]:
        if r == self.n - 1:
            for i in range(self.n):
                if board[r][i] != '.':
                    board[r][i] = "Q"
                    return board
            return [[]]
        ans = []
        for i in range(self.n):
            if board[r][i] != ".":
                temp_board = [[*k] for k in board]
                temp_board[r][i] = "Q"
                self.checkAndElemenate(r, i, temp_board)
                child = self.recursive(r + 1, temp_board)
                if child[0]:
                    ans += child
        return ans if ans else [[]]

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        ans = []
        if (x := self.recursive(0, [['' for _ in range(n)] for __ in range(n)]))[0]:
            i = 0
            while i < len(x):
                if not i % n:
                    ans.append([])
                ans[-1].append("".join(x[i]))
                i += 1
        return ans


S = Solution()
X = S.solveNQueens(100)
print(X)
