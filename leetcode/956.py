# https://leetcode.com/problems/tallest-billboard/
import random

from USEFUL_CODES.LC import *


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        """
        time: O(n*k) where k is sum(rods)
        :param rods:
        :return:
        """
        n = len(rods)
        h = sum(rods) // 2

        @cache
        def DP(i, s):
            if s > h:
                return -1
            if i == n:
                if not s:
                    return 0
                return -1
            t1 = DP(i + 1, s + rods[i])
            if t1 >= 0:
                t1 += rods[i]
            t2 = DP(i + 1, s - rods[i])
            t3 = DP(i + 1, s)

            lans = t1
            if t2 > lans:
                lans = t2
            if t3 > lans:
                lans = t3
            return lans

        return DP(0, 0)

    def tallestBillboard2(self, rods):
        """
        Editorial sol of O(3^(n/2))
        :param rods:
        :return:
        """
        # Helper function to collect every combination `(left, right)`
        def helper(half_rods):
            states = set()
            states.add((0, 0))
            for r in half_rods:
                new_states = set()
                for left, right in states:
                    new_states.add((left + r, right))
                    new_states.add((left, right + r))
                states |= new_states

            dp = {}
            for left, right in states:
                dp[left - right] = max(dp.get(left - right, 0), left)
            return dp

        n = len(rods)
        first_half = helper(rods[:n // 2])
        second_half = helper(rods[n // 2:])

        answer = 0
        for diff in first_half:
            if -diff in second_half:
                answer = max(answer, first_half[diff] + second_half[-diff])
        return answer

    def tallestBillboard3(self, rods: List[int]) -> int:
        """
        Editorial sol of O(n * sum(rods))
        :param rods:
        :return:
        """
        # dp[taller - shorter] = taller
        dp = {0: 0}

        for r in rods:
            # dp.copy() means we don't add r to these stands.
            new_dp = dp.copy()
            for diff, taller in dp.items():
                shorter = taller - diff

                # Add r to the taller stand, thus the height difference is increased to diff + r.
                new_dp[diff + r] = max(new_dp.get(diff + r, 0), taller + r)

                # Add r to the shorter stand, the height difference is expressed as abs(shorter + r - taller).
                new_diff = abs(shorter + r - taller)
                new_taller = max(shorter + r, taller)
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_taller)

            dp = new_dp

        # Return the maximum height with 0 difference.
        return dp.get(0, 0)

S = Solution()
rod = [random.randint(1,1000) for _ in range(20)]
print(max(rod),min(rod),sum(rod))
X = S.tallestBillboard(rod)
Y = S.tallestBillboard3(rod)
# Z = S.tallestBillboard2(rod)
print(X,Y)