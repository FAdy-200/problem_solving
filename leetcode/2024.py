# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/
from USEFUL_CODES.LC import *


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def helper(ele: str) -> int:
            window = [0, 0]
            ans = 0
            l_k = k
            while window[-1] < len(answerKey):
                if answerKey[window[-1]] == ele:
                    window[-1] += 1
                elif l_k:
                    window[-1] += 1
                    l_k -= 1
                else:
                    while answerKey[window[0]] == ele:
                        window[0] += 1
                        if window[0] > window[1]:
                            window[1] += 1
                    window[0] += 1
                    if window[0] > window[1]:
                        window[1] += 1
                    l_k += 1
                    l_k = k if l_k > k else l_k
                ans = ans if ans > (z := window[1] - window[0]) else z
            return ans
        return max(helper("T"), helper("F"))