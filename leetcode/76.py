# https://leetcode.com/problems/minimum-window-substring/
from collections import defaultdict
from copy import copy


class Solution:

    def helper(self, s, t, freq_s, freq_t) -> str:
        i = 0
        j = len(s) - 1
        while j > i - 1:
            if freq_t[s[i]] == 0:
                i += 1
                continue
            if freq_t[s[j]] == 0:
                j -= 1
                continue
            if freq_s[s[i]] > freq_t[s[i]]:
                if freq_s[s[j]] > freq_t[s[j]]:
                    freq_s[s[i]] -= 1
                    t1 = self.helper(s[i + 1:j + 1], t, copy(freq_s), copy(freq_t))
                    freq_s[s[i]] += 1
                    freq_s[s[j]] -= 1
                    t2 = self.helper(s[i:j], t, copy(freq_s), copy(freq_t))
                    return t1 if len(t1) < len(t2) else t2
                else:
                    freq_s[s[i]] -= 1
                    i += 1
                    continue
            elif freq_s[s[j]] > freq_t[s[j]]:
                freq_s[s[j]] -= 1
                j -= 1
                continue
            else:
                for m, n in freq_t.items():
                    if freq_s[m] < n:
                        return ""
                return s[i:j + 1]

        return ""

    def minWindow1(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        freq_s = defaultdict(lambda: 0)
        freq_t = defaultdict(lambda: 0)
        for i in s:
            freq_s[i] += 1
        for j in t:
            freq_t[j] += 1
        return self.helper(s, t, freq_s, freq_t)

    @staticmethod
    def check(freq_s, freq_t):
        for i, j in freq_t.items():
            if freq_s[i] < j:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        freq_t = defaultdict(lambda: 0)
        for j in t:
            freq_t[j] += 1
        freq_s = defaultdict(lambda: 0)
        ans = [float("inf"), None, None]
        i = 0
        j = 1
        freq_s[s[0]] += 1
        while len(s) + 1 > j > i:
            z = s[i:j]
            if self.check(freq_s, freq_t):
                if j - i < ans[0]:
                    ans[0] = j - i
                    ans[1] = i
                    ans[2] = j
                freq_s[s[i]] -= 1
                i += 1
            else:
                freq_s[s[j:j + 1]] += 1
                j += 1
        return s[ans[1]:ans[2]] if ans[1] is not None else ""


S = Solution()
x = S.minWindow(
    "ADOBECODEBANC",
    "ABC")
print(x)
