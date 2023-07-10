# https://leetcode.com/problems/put-marbles-in-bags/
from USEFUL_CODES.LC import *


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        s_weights_f = []
        for i in range(n - 1):
            s_weights_f.append(weights[i] + weights[i + 1])
        s_weights_f.sort()
        s_weights_b = s_weights_f[::-1]

        answer = 0
        for i in range(k - 1):
            answer += s_weights_b[i] - s_weights_f[i]

        return answer


S = Solution()
X = S.putMarbles([1, 3, 5, 1], 2)
print(X)
