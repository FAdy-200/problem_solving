# https://leetcode.com/problems/string-compression/
from USEFUL_CODES.LC import *


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        write_at = 0
        slow = 0
        fast = 0
        while fast < len(chars):
            if chars[fast] == chars[slow]:
                fast += 1
            else:
                if fast-slow > 1:
                    chars[write_at] = f"{chars[slow]}"
                    chars[write_at+1] = f"{fast-slow}"
                    write_at += 2
                else:
                    chars[write_at] = f"{chars[slow]}"
                    write_at += 1
                slow = fast
        if fast - slow > 1:
            chars[write_at] = f"{chars[slow]}"
            chars[write_at + 1] = f"{fast - slow}"
            write_at += 2
        else:
            chars[write_at] = f"{chars[slow]}"
            write_at += 1
        chars[:write_at] = list((z:="".join(chars[:write_at])))
        return len(z)





S = Solution()
chars = ["a","a","a","a","a","b"]
X = S.compress(chars)
print(X)
