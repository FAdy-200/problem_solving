# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/
from USEFUL_CODES.LC import *


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        root = create_BST(nums)
        MOD = 10 ** 9 + 7

        def dfs(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return [0, 1]
            if not node.right and not node.left:
                return [1, 1]

            left = dfs(node.left)
            right = dfs(node.right)
            return [left[0] + right[0] + 1, (comb(right[0] + left[0], right[0]) * left[1] * right[1]) % MOD]

        return dfs(root)[1] - 1


S = Solution()
X = S.numOfWays([1, 2, 4, 6, 7, 10, 5, 9, 3, 8])
print(X)
