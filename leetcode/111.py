# https://leetcode.com/problems/minimum-depth-of-binary-tree/
from USEFUL_CODES.LC import *


class Solution:
    def minDepth(self, root: Optional[BiTreeNode]) -> int:
        if not root:
            return 0
        d: Deque[Tuple[BiTreeNode, int]] = deque()
        d.append((root, 1))
        while d:
            node, lvl = d.popleft()
            if not node.left and not node.right:
                return lvl
            if node.left:
                d.append((node.left, lvl + 1))
            if node.right:
                d.append((node.right, lvl + 1))

tree = create_tree([3,9,20,null,null,15,7])
S = Solution()
X = S.minDepth(tree)
print(X)
