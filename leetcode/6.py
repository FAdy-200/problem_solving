# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        ans = [[""] for _ in range(numRows)]
        j = 0
        state = 1
        for i in range(n):
            ans[j].append(s[i])
            if state > 0:
                j += 1
                if j == numRows - 1:
                    state *= -1
            else:
                j -= 1
                if not j:
                    state *= -1

        return "".join([i for m in ans for i in m])


S = Solution()
X = S.convert("AB", 3)
print(X)
