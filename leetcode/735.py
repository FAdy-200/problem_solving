# https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75
from USEFUL_CODES.LC import *


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = [asteroids[0]]
        for i in asteroids[1:]:
            if st and st[-1] > 0 > i:
                while st and i < 0 < st[-1] < -i:
                    st.pop()
                if st and st[-1] < 0:
                    st.append(i)
                if st and st[-1] == -i:
                    st.pop()
                elif not st:
                    st.append(i)

            else:
                st.append(i)

        return st

S = Solution()
X = S.asteroidCollision([1,-1,-2,-2])
print(X)
