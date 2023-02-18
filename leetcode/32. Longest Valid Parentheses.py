# https://leetcode.com/problems/longest-valid-parentheses/
from typing import *
from collections import *

class Solution:

    def longestValidParentheses(self, s: str) -> int:
        s = s.lstrip(')')
        s = s.rstrip('(')
        t = []
        sol = []
        previous = ""

        for i, j in enumerate(s):
            if j == previous:
                pass
            else:
                previous = j
                t.append(i)
        t.append(len(s))
        av = 0
        start = []
        for i in range(1, len(t), 2):
            if not av:
                sol.append([min(t[i] - t[i - 1], t[i + 1] - t[i]), 0])
                if t[i] - t[i - 1] >= t[i + 1] - t[i]:
                    av = 1
                    if t[i] - t[i - 1] - min(t[i] - t[i - 1], t[i + 1] - t[i]):
                        start.append(t[i] - t[i - 1] - min(t[i] - t[i - 1], t[i + 1] - t[i]))
            else:
                if t[i] - t[i - 1] <= t[i + 1] - t[i]:
                    ad = min(t[i] - t[i - 1], t[i + 1] - t[i])
                    sol[-1][0] += ad
                    if t[i] - t[i - 1] == t[i + 1] - t[i]:
                        av = 1
                    else:
                        new = t[i + 1] - t[i] - ad
                        if start:
                            ad = min(start[-1], new)
                            sol[-1][0] += ad
                            new -= ad
                            start[-1] -= ad
                            while len(start) > 1 and not start[-1]:
                                start.pop()
                                temp = sol.pop()
                                if sol and sol[-1][1]:
                                    sol[-1][0] += temp[0]
                                else:
                                    sol.append(temp)
                                if new:
                                    ad = min(start[-1], new)
                                    sol[-1][0] += ad
                                    new -= ad
                                    start[-1] -= ad
                            while len(start) and not start[-1]:
                                start.pop()
                                temp = sol.pop()
                                if sol and sol[-1][1]:
                                    sol[-1][0] += temp[0]
                                else:
                                    sol.append(temp)
                            if new:
                                av = 0
                            else:
                                av = 1
                        else:
                            av = 0
                else:
                    sol.append([min(t[i] - t[i - 1], t[i + 1] - t[i]), 0])
                    av = 1
                    if t[i] - t[i - 1] - min(t[i] - t[i - 1], t[i + 1] - t[i]):
                        start.append(t[i] - t[i - 1] - min(t[i] - t[i - 1], t[i + 1] - t[i]))
            sol[-1][1] = av
        return max(sol, key=lambda x: x[0])[0] * 2 if sol else 0

    def new(self, s: str) -> int:
        st = []
        length = 0
        st.append(-1)
        for i in range(len(s)):
            if(s[i] == "("):
                st.append(i)
            else:
                st.pop()
                if(not st):
                    st.append(i)
                length = max(length, i-st[-1])
        return length


S = Solution()
x = S.longestValidParentheses("()))(()(()))(")
print(x)
