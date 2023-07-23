# https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l_s = s.split()
        if len(pattern) != len(l_s):
            return False
        seen = set()
        m = {}
        for i in range(len(l_s)):
            if m.get(pattern[i]) is not None:
                if m[pattern[i]] != l_s[i]:
                    return False
            else:
                if l_s[i] not in seen:
                    m[pattern[i]] = l_s[i]
                    seen.add(l_s[i])
                else:
                    return False
        return True


S = Solution()
X = S.wordPattern("abba", "dog dog dog dog")
print(X)
