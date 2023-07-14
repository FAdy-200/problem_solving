# https://leetcode.com/problems/path-sum-iii/?envType=study-plan-v2&envId=leetcode-75
from USEFUL_CODES.LC import *


# TODO: Finish this later
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        seen = set()

        def dfs(node: TreeNode, so_far: int) -> int:
            if not node or (x := (id(node), so_far)) in seen:
                return 0
            seen.add(x)
            ans = 0
            so_far -= node.val
            if not so_far:
                ans = 1
            if node.left:
                temp = dfs(node.left, so_far)
                ans += temp
                if so_far != targetSum:
                    ans += dfs(node.left, targetSum)
                else:
                    ans += temp
            if node.right:
                temp = dfs(node.right, so_far)
                ans += temp
                if so_far != targetSum:
                    ans += dfs(node.right, targetSum)
                else:
                    ans += temp

            return ans

        return dfs(root, targetSum)


S = Solution()
tree = create_tree([0, 1, 1])
X = S.pathSum(tree, 0)
print(X)
