# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        ans = 1

        while j < len(s):
            if s[j] != s[i]:
                j += 1
                ans = max(ans, j - i)
            else:
                i += 1
                j += 1
        return ans


S = Solution()
x = S.lengthOfLongestSubstring("abcabcbb")
print(x)
