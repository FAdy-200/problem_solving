from typing import Optional,List
from collections import deque

null = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left:Optional[TreeNode] = None
        self.right:Optional[TreeNode] = None

    def __repr__(self):
        return self.val

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
        if arr[i]:
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


if __name__ == "__main__":
    class t1:
        def __init__(self, x):
            self.x = x

        def __repr__(self):
            return self.x

        def __hash__(self):
            return hash(self.x)

        def __eq__(self, other):
            return self.x == other.x
    class t2:
        def __init__(self, x):
            self.x = x

        def __repr__(self):
            return self.x

        def __hash__(self):
            return hash(self.x)

        def __eq__(self, other):
            return self.x == other.x

    x1 = t1("2")
    x2 = t2("2")
    asd = set()
    asd.add(x1)
    print(x2 in asd)
    # test = [5, 3, 6, 2, 4, null, 5, 1]
    # create_tree(test)
