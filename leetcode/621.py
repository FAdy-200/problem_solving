# https://leetcode.com/problems/task-scheduler/
from typing import *
from collections import defaultdict


class Solution:
    def leastInterval1(self, tasks: List[str], n: int) -> int:
        if not n:
            return len(tasks)
        freq = defaultdict(lambda: 0)
        ans = 0
        for i in tasks:
            freq[i] += 1
        temp = list(sorted(list(map(list, freq.items())), key=lambda x: x[1], reverse=True))
        print(temp)
        while temp:
            t = 0
            for i, j in enumerate(temp):
                if j[1]:
                    t += 1
                    j[1] -= 1
                if t == n + 1:
                    temp = list(sorted(temp, key=lambda x: x[1], reverse=True))
                    break
            for i in temp[::-1]:
                if not i[1]:
                    temp.pop()
            if t < n + 1 and temp:
                t = n + 1
            ans += t
        return ans

    def leastInterval(self, tasks: List[str], n: int) -> int:
        numTasks = len(tasks)
        taskToCount = {}
        for task in tasks:
            currentCount = taskToCount.setdefault(task, 0)
            taskToCount[task] = currentCount + 1
        counts = sorted(taskToCount.values(), reverse=True)
        spotsToFill = n * (counts[0] - 1)
        for i in range(1, len(counts)):
            if spotsToFill <= 0:
                return numTasks
            x,y = counts[i], counts[0] - 1
            spotsToFill -= min(counts[i], counts[0] - 1)
        return numTasks + spotsToFill


S = Solution()
X = S.leastInterval(["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], 2)
print(X)
