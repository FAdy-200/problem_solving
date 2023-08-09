from collections import deque
from typing import Optional, List

null = None


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.numberOfOccurrences = 1
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right

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


def create_bst(arr: List[int]) -> Optional[TreeNode]:
    if not arr:
        return
    head = TreeNode(arr[0])
    for i in arr[1:]:
        add_BST(head, i)
    return head


def add_bst(root: Optional[TreeNode], val: int) -> None:
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


def copy_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    new_tree = TreeNode(root.val)

    def dfs(orig: Optional[TreeNode], copy: Optional[TreeNode]):
        if orig.left:
            copy.left = TreeNode(orig.left.val)
            dfs(orig.left, copy.left)
        if orig.right:
            copy.right = TreeNode(orig.right.val)
            dfs(orig.right, copy.right)

    dfs(root, new_tree)
    return new_tree


def check_equal(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    if not root1 and not root2:
        return True
    if root2 and root1:
        if root2.val != root1.val:
            return False
        if not check_equal(root1.left, root2.left):
            return False
        if not check_equal(root1.right, root2.right):
            return False
        return True
    return False


def delete_val_bst(root:Optional[TreeNode], val:int) -> Optional[TreeNode]:
    pass