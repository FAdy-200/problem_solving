# https://leetcode.com/problems/valid-sudoku/
from typing import *
from collections import defaultdict


class Solution:
    def check(self, array):
        for i in array:
            co = defaultdict(lambda: 0)
            for j in i:
                if j != ".":
                    co[j] += 1
            if not len(co.values()):
                continue
            if max(co.values()) > 1:
                return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = list(zip(*board))
        boxes = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                boxes.append([])
                for m in range(3):
                    boxes[-1] += board[i+m][j:j+3]
        return self.check(board) and self.check(col) and self.check(boxes)


S = Solution()
x = S.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
print(x)
