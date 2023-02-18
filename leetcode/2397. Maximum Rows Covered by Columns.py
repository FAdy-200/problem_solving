from typing import *


class Solution:
    def __init__(self):
        self.memo = {}

    def recursiveSolution(self, matrix, numSelect,):
        if self.memo.get((matrix,numSelect)) is not None:
            return self.memo.get((matrix,numSelect))
        if not numSelect:
            return 0
        zeroCount = [sum(i) for i in matrix]
        

        

    def maximumRows2(self, matrix: List[List[int]], numSelect: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if numSelect >= n:
            return m
        return self.recursiveSolution(tuple(map(tuple,matrix)), numSelect,0)


    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if numSelect >= n:
            return m
        sums = [0]*n
        for k in matrix:
            for i,j in enumerate(k):
                sums[i]+=j
        sums = list(sorted(enumerate(sums),key=lambda x:x[1],reverse=True))
        matrixT = list(map(list, zip(*matrix)))
        for i in sums[:numSelect]:
            matrixT[i[0]] = [0] * m
        matrix = list(map(list, zip(*matrixT)))
        sol = 0
        for k in matrix:
            if not sum(k):
                sol+=1
        return sol



s = Solution()
x = s.maximumRows([[1,0,1,1,1,1],[0,0,0,1,1,0],[1,1,0,0,0,0],[0,0,1,1,0,1]], 2)
print(x)