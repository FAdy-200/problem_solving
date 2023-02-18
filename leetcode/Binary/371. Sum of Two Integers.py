# https://leetcode.com/problems/sum-of-two-integers/


class Solution:
    def getSum(self, a: int, b: int) -> int:
        c = "0"
        if a < 0 or b < 0:
            c = "1"
            a = abs(a)
            b = abs(b)
        a = bin(a)[:1:-1]
        b = bin(b)[:1:-1]
        a += "0" * max(0, len(b) - len(a))
        b += "0" * max(0, len(a) - len(b))
        ans = ""
        for i in range(len(a)):
            t1 = int(a[i]) ^ int(b[i])
            t2 = t1 ^ int(c)
            ans += str(t2)
            c = str((a[i] + b[i] + c).count("1") // 2)
        if int(c):
            ans += c

        return int(ans[::-1], 2)


s = Solution()
print(s.getSum(-1, 1))

