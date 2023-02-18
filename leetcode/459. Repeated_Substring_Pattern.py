# https://leetcode.com/problems/repeated-substring-pattern/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        checked = set()
        ma = len(s)
        if ma < 3:
            if ma == 1:
                return False
            return True if s[0] == s[1] else False
        for i in range(1, len(s)):
            if i in checked:
                continue
            if ma / i == int(ma / i):
                checked.add(i)
                new = s[:i] * int(ma / i)
                if new == s:
                    return True
        return False


s = Solution()
print(s.repeatedSubstringPattern("abcabc"))
