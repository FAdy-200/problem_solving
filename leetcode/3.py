# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 1
        i = 0
        j = 1
        n = len(s)
        if not n:
            return 0
        while j < n:
            try:
                p = s[i:j].index(s[j]) + i
            except ValueError:
                p = None
            if p is None:
                j += 1
            else:
                i = p + 1
            ans = max(ans, j - i)
        return ans


S = Solution()
x = S.lengthOfLongestSubstring("")
print(x)
