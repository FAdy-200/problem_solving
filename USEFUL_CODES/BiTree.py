from typing import Optional, List
from collections import deque

null = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.numberOfOccurrences = 1
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.val)


def create_tree(arr: List[int]) -> Optional[TreeNode]:
    if not arr:
        return
    head = TreeNode(arr[0])
    if len(arr) == 1:
        return head
    nodes = deque()
    nodes.append(head)
    i = 1
    while i < len(arr):
        if arr[i] is not null:
            if i % 2:
                nodes[0].left = TreeNode(arr[i])
                nodes.append(nodes[0].left)
            else:
                nodes[0].right = TreeNode(arr[i])
                nodes.append(nodes[0].right)
                nodes.popleft()
        else:
            if not i % 2:
                nodes.popleft()
        i += 1
    return head


def create_BST(arr: List[int]) -> Optional[TreeNode]:
    if not arr:
        return
    head = TreeNode(arr[0])
    for i in arr[1:]:
        add_BST(head, i)
    return head


def add_BST(root: Optional[TreeNode], val: int) -> None:
    if val == root.val:
        root.numberOfOccurrences += 1
        return
    par = temp = root
    if val > temp.val:
        temp = temp.right
    else:
        temp = temp.left
    while temp:
        par = temp
        if val > temp.val:
            temp = temp.right
        else:
            temp = temp.left
    if val > par.val:
        par.right = TreeNode(val)
    elif val == par.val:
        par.numberOfOccurrences += 1
    else:
        par.left = TreeNode(val)
