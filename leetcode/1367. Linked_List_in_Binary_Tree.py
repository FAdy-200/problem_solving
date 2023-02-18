from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


def makeLL(x):
    Head = ListNode(x[0])
    temp = Head
    for i in x[1:]:
        Node = ListNode(i)
        temp.next = Node
        temp = Node
    return Head


def makeTree():
    # FIXME THIS IS STUPID
    Head = TreeNode(1)
    Node1 = TreeNode(5)
    Head.right = Node1
    node2 = TreeNode(10)
    node3 = TreeNode(9)
    Node1.left = node2
    Node1.right = node3
    node4 = TreeNode(5)
    node5 = TreeNode(2)
    node2.right = node4
    node4.left = node5
    return Head


S = Solution()
x = S.isSubPath(makeLL([1, 5, 2]), makeTree())
print(x)
