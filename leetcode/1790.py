class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s = ["", ""]
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s[0] and (s[0] != s2[i] or s1[i] != s[1]):
                    return False
                elif not s[0]:
                    s = [s1[i], s2[i]]
                else:
                    s = ["$", "$"]
        return True if s[0] == "$" or not s[0] else False


S = Solution()
X = S.areAlmostEqual("ca", "ac")
print(X)
