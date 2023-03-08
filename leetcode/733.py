# https://leetcode.com/problems/flood-fill/
from typing import *


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        nodes = [(sr, sc)]
        seen = set()
        seen.add((sr, sc))
        while nodes:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if abs(i) == abs(j):
                        continue
                    if len(image) > nodes[0][0] + i > -1:
                        if len(image[0]) > nodes[0][1] + j > -1:
                            if image[nodes[0][0] + i][nodes[0][1] + j] == image[nodes[0][0]][nodes[0][1]]:
                                if (nodes[0][0] + i, nodes[0][1] + j) not in seen:
                                    seen.add((nodes[0][0] + i, nodes[0][1] + j))
                                    nodes.append((nodes[0][0] + i, nodes[0][1] + j))
                    else:
                        break
            image[nodes[0][0]][nodes[0][1]] = color
            nodes.pop(0)
        return image

S = Solution()
X = S.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0)
print(X)
