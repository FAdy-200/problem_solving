# https://leetcode.com/problems/reorganize-string/

from collections import defaultdict
import heapq


class Solution:
    def reorganizeString1(self, s: str) -> str:
        freq = defaultdict(lambda: 0)
        ans = ""
        for i in s:
            freq[i] += 1
        temp = list(sorted(list(map(list, freq.items())), key=lambda x: x[1], reverse=True))
        while len(ans) < len(s):
            temp = list(sorted(temp, key=lambda x: x[1], reverse=True))
            ans += temp[0][0]
            temp[0][1] -= 1
            temp = list(sorted(temp, key=lambda x: x[1], reverse=True))
            if len(ans) == len(s):
                return ans
            if ans[-1] == temp[0][0]:
                if not len(temp) > 1:
                    return ""
                if temp[1][1] > 0:
                    ans += temp[1][0]
                    temp[1][1] -= 1
                else:
                    return ""
        return ans

    def reorganizeString(self, s: str) -> str:
        freq = defaultdict(lambda: 0)
        ans = ""
        for i in s:
            freq[i] -= 1
        heap = []
        for i, j in freq.items():
            heapq.heappush(heap, (j, i))
        while len(heap) > 1:
            t1 = heapq.heappop(heap)
            t2 = heapq.heappop(heap)
            ans += t1[1] + t2[1]
            if t1[0] < -1:
                heapq.heappush(heap, (t1[0] + 1, t1[1]))
            if t2[0] < -1:
                heapq.heappush(heap, (t2[0] + 1, t2[1]))

        if heap:
            t = heap.pop()
            if t[0] == -1:
                ans += t[1]
            else:
                return ""
        return ans
S = Solution()
X = S.reorganizeString("vvvlo")
print(X)
