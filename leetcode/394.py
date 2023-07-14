# https://leetcode.com/problems/decode-string/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def decodeString(self, s: str) -> str:
        st1 = [""]
        st2 = [""]
        for i in s:
            if i == "[":
                st1.append("")
                st2.append("")
            elif i == "]":
                last = st2.pop()
                st2[-1] += last * int(st1[-2])
                st1.pop(-2)
            elif i.isdigit():
                st1[-1] += i
            else:
                st2[-1] += i
        return st2[0]

S = Solution()
X = S.decodeString("2[abc]3[cd2[ma]]ef")
print(X)
