# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
from typing import *
from USEFUL_CODES.BiTree import *


class Solution:
    def __init__(self):
        self.found = 0

    def lowestCommonAncestor(self, root: 'TreeNode', p: Optional['TreeNode'], q: Optional['TreeNode']) -> Optional[
        'TreeNode']:
        # self.helper(root,p,q)
        # return self.ans
        if not root:
            return
        if root == q and not p:
            return root
        if root == p and not q:
            return root
        if root == p and q:
            l = self.lowestCommonAncestor(root.left, None, q)
            if l:
                self.found = 1
            r = self.lowestCommonAncestor(root.right, None, q)
            if r:
                self.found = 1
            return root
        if root == q and p:
            l = self.lowestCommonAncestor(root.left, p, None)
            if l:
                self.found = 1
            r = self.lowestCommonAncestor(root.right, p, None)
            if r:
                self.found = 1
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        if l:
            if l == p:
                if self.found:
                    return l
                r = self.lowestCommonAncestor(root.right, None, q)
                if r:
                    self.found = 1
                    return root
                return l
            elif l == q:
                if self.found:
                    return l
                r = self.lowestCommonAncestor(root.right, p, None)
                if r:
                    self.found = 1
                    return root
                return l
            else:
                return l
        return self.lowestCommonAncestor(root.right, p, q)


S = Solution()
tree = create_tree([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4])
X = S.lowestCommonAncestor(tree, tree.left, tree.right.right)
print(X)
