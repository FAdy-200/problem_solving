# https://leetcode.com/problems/add-binary/?envType=study-plan&id=programming-skills-ii

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b)>=len(a):
            num1 = a[::-1]
            num2 = b[::-1]
        else:
            num1 = b[::-1]
            num2 = a[::-1]
        ans = []
        carry = 0
        i = 0
        while i < len(num1):
            if num1[i] == "1" and num2[i] == "1" and carry:
                ans.append("1")
            elif num1[i] == "1" and num2[i] == "1":
                carry = 1
                ans.append("0")
            elif (num1[i] == "1" or num2[i] == "1") and carry:
                carry = 0
                ans.append("0")
            elif (num1[i] == "1" or num2[i] == "1"):
                carry = 0
                ans.append("1")
            elif carry:
                carry = 0
                ans.append("1")
            else:
                ans.append("0")
            i+=1
        if carry:
            while i < len(num2):
                if carry and num2[i] == "1":
                    ans.append("0")
                elif carry:
                    ans.append("1")
                    ans+=num2[i+1:]
                    return "".join(ans[::-1])
                i+=1
        else:
            ans+=num2[i:]
            return "".join(ans[::-1])

        if carry:
            ans.append("1")
        return "".join(ans[::-1])


S = Solution()
x = S.addBinary("110010","10111"
)
print(x)
