# https://leetcode.com/problems/detonate-the-maximum-bombs/
from typing import List, DefaultDict, Set
from collections import defaultdict, deque
from math import sqrt


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        if len(bombs) == 1:
            return 1
        graph: DefaultDict[int, Set[int]] = defaultdict(set)

        for i, val in enumerate(bombs):
            for j, val2 in enumerate(bombs[i + 1:]):
                if (dist := sqrt((val[0] - val2[0]) ** 2 + (val[1] - val2[1]) ** 2)) <= val[2]:
                    graph[i].add(j + i + 1)
                if dist <= val2[2]:
                    graph[j + i + 1].add(i)

        seen = set()
        ans = 1
        nodes = list(graph.keys())
        for i in nodes:
            if i not in seen:
                temp_ans = 0
                d = deque()
                d.append(i)
                seen.add(i)
                small_seen = set()
                small_seen.add(i)
                while d:
                    temp_ans += 1
                    node = d.popleft()
                    for j in graph[node]:
                        if j not in small_seen:
                            d.append(j)
                            small_seen.add(j)
                ans = max(ans, temp_ans)
        return ans


S = Solution()
X = S.maximumDetonation(
    [[6, 874, 154], [214, 633, 233], [786, 52, 144], [62, 561, 134], [643, 144, 17], [609, 578, 432], [553, 548, 433],
     [237, 992, 472], [16, 588, 323], [984, 826, 50], [210, 694, 143], [758, 74, 24], [363, 173, 116], [121, 741, 332],
     [274, 97, 147]])
print(X)
