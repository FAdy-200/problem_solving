# https://leetcode.com/problems/daily-temperatures/?envType=study-plan&id=programming-skills-ii

from typing import *
import bisect

class Solution:
    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
        sorted_temps = sorted(enumerate(temperatures), key=lambda x: x[1],reverse=True)\
            # [::-1]
        ans = [0]*len(temperatures)
        mi = [sorted_temps[0][0]]
        temp = sorted_temps[0]
        for i in sorted_temps[1:]:
            if i[1] == temp[1]:
                ans[i[0]] = ans[temp[0]]
                mi.append(i[0])
            if i[1] < temp[1]:
                small = float("inf")
                for j in mi:
                    if not i[0]:
                        small = min(mi)
                        break
                    x = j-i[0]
                    if x > 0:
                        if x < small:
                            small = x
                ans[i[0]] = small if small != float("inf") else 0
                mi.append(i[0])
            else:
                small = float("inf")
                for j in mi:
                    if not i[0]:
                        small = min(mi)
                        break
                    x = j-i[0]
                    if x > 0:
                        if x < small:
                            small = x
                ans[i[0]] = small if small != float("inf") else 0
                mi[-1] = min(mi[-1], i[0])
            temp = i

        ans[-1] = 0
        return ans


    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sorted_temps = sorted(enumerate(temperatures), key=lambda x: x[1],reverse=True)\
            # [::-1]
        ans = [0]*len(temperatures)
        mi = [sorted_temps[0][0]]
        temp = sorted_temps[0]
        for i in sorted_temps[1:]:
            if i[1] == temp[1]:
                ans[i[0]] = ans[temp[0]]
            if i[1] <= temp[1]:
                small = bisect.bisect(mi, i[0])
                small = 0 if small == -1 else small
                ans[i[0]] = mi[small]-i[0] if small < len(mi) else 0
            bisect.insort(mi, i[0])
            temp = i

        ans[-1] = 0
        return ans



# [1,1,4,2,1,1,0,0]


S = Solution()
z = S.dailyTemperatures([73,74,75,71,69,72,76,73])
print(z)
