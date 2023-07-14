# https://leetcode.com/problems/linked-list-in-binary-tree/
from USEFUL_CODES.LC import *




class Solution:
    def __init__(self):
        self.d = {}

    def helper(self, head: Optional[ListNode], root: Optional[TreeNode], streak=False):
        if self.d.get((head, root)) is not None:
            return self.d[(head, root)]
        if head is None:
            self.d[(head, root)] = True, False
            return self.d[(head, root)]
        if root is None:
            self.d[(head, root)] = False, False
            return self.d[(head, root)]
        if head.val == root.val:
            ans1 = self.helper(head.next, root.left, True)
            ans2 = self.helper(head.next, root.right, True)
            if ans1[0] | ans2[0]:
                self.d[(head, root)] = True, False
                return self.d[(head, root)]
            elif ans1[1] and ans2[1]:
                if not streak:
                    ans1 = self.helper(head, root.left)
                    ans2 = self.helper(head, root.right)
                    self.d[(head, root)] = ans1[0] | ans2[0], ans1[1] | ans2[1]
                    return self.d[(head, root)]
                return ans1
            elif ans2[1]:
                self.d[(head, root)] = self.helper(head, root.right)
            elif ans1[1]:
                self.d[(head, root)] = self.helper(head, root.left)
        if streak:
            self.d[(head, root)] = False, True
            return self.d[(head, root)]
        ans1 = self.helper(head, root.left)
        ans2 = self.helper(head, root.right)
        self.d[(head, root)] = ans1[0] | ans2[0], False
        return self.d[(head, root)]

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        return self.helper(head, root)[0]





S = Solution()
x = S.isSubPath(create_linked_list([1,4,2,6]), create_tree([1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]))
print(x)
