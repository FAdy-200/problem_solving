# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
from USEFUL_CODES.LC import *


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        srt_obs = []
        dp: DefaultDict[int, int] = defaultdict(int)
        ans = []
        for i in obstacles:
            if i not in dp:
                pos = bisect.bisect_left(srt_obs, i)
                srt_obs.insert(pos,i)
            else:
                pos = bisect.bisect_left(srt_obs, i)
            if (t := pos) != 0:
                t -= 1
            dp[i] = max(dp[srt_obs[t]] + 1, dp[i] + 1)
            pos += 1
            while pos<len(srt_obs) and dp[srt_obs[pos]] <= dp[i]:
                dp.pop(srt_obs.pop(pos))
            ans.append(dp[i])
        return ans


S = Solution()
with open("1964.txt","r") as inp:
    p1 = eval(inp.readline())
X = S.longestObstacleCourseAtEachPosition(p1)
print(X)
# [1, 1, 2, 3, 2, 3, 4, 5, 3, 5]
