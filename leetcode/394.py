# https://leetcode.com/problems/decode-string/?envType=study-plan-v2&envId=leetcode-75

# TODO: Finish this later
class Solution:
    def decodeString(self, s: str) -> str:
        st1 = []
        st2 = []
        i = 0
        ans = ""
        while i < len(s):
            if s[i].isdigit():
                j = i+1
                while j < len(s) and s[j].isdigit():
                    j+=1
                st1.append(int(s[i:j]))
                i = j - 1
            elif s[i] == "[":
                st2.append(i + 1)
            elif s[i] == "]":
                ans += st1.pop() * s[st2.pop():i]
            elif not st1:
                ans += s[i]
            i += 1
        return ans



S = Solution()
X = S.decodeString("2[abc]3[cd]ef")
print(X)
