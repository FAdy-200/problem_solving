# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/?envType=study-plan-v2&envId=leetcode-75
from USEFUL_CODES.LC import *


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def zig(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            t1 = zag(node.right) + 1
            t2 = zig(node.left)

        def zag(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            t1 = zig(node.left) + 1
            t2 = zag(node.right)

        return max(zig(root), zag(root))


S = Solution()
tree = create_tree([1, null, 1, 1, 1, null, null, 1, 1, null, 1, null, null, null, 1])
X = S.longestZigZag(tree)
print(X)
