# https://leetcode.com/problems/shortest-path-to-get-all-keys/
from USEFUL_CODES.LC import *


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        seen: DefaultDict[int, Set] = defaultdict(set)
        key_set, lock_set = set(), set()
        all_keys = 0
        start = (-1, -1)
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item in 'abcdef':
                    all_keys += (1 << (ord(item) - ord('a')))
                    key_set.add(item)
                if item in 'ABCDEF':
                    lock_set.add(item)
                if item == "@":
                    start = (i, j)

        queue.append(start + (0, 0))
        seen[0].add(start)
        while queue:
            cur_i, cur_j, keys, dist = queue.popleft()
            for x, y in ((cur_i, cur_j + 1), (cur_i + 1, cur_j), (cur_i - 1, cur_j), (cur_i, cur_j - 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] != '#':
                    cell = grid[x][y]
                    if cell in key_set and not ((1 << (ord(cell) - ord('a'))) & keys):
                        new_keys = (keys | (1 << (ord(cell) - ord('a'))))

                        if new_keys == all_keys:
                            return dist + 1
                        seen[new_keys].add((x, y))
                        queue.append((x, y, new_keys, dist + 1))
                    elif cell in lock_set and not (keys & (1 << (ord(cell) - ord('A')))):
                        continue
                    elif (x, y) not in seen[keys]:
                        seen[keys].add((x, y))
                        queue.append((x, y, keys, dist + 1))
        return -1


S = Solution()
X = S.shortestPathAllKeys(["@cCaA", "dDB#e", "EfF.b"])
print(X)
