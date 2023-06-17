from typing import Optional, List
from collections import deque

null = None


class BiTreeNode:
    def __init__(self, x):
        self.val = x
        self.left: Optional[BiTreeNode] = None
        self.right: Optional[BiTreeNode] = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.val)


def create_tree(arr: List[int]) -> Optional[BiTreeNode]:
    if not arr:
        return
    head = BiTreeNode(arr[0])
    if len(arr) == 1:
        return head
    nodes = deque()
    nodes.append(head)
    i = 1
    while i < len(arr):
        if arr[i] is not null:
            if i % 2:
                nodes[0].left = BiTreeNode(arr[i])
                nodes.append(nodes[0].left)
            else:
                nodes[0].right = BiTreeNode(arr[i])
                nodes.append(nodes[0].right)
                nodes.popleft()
        else:
            if not i % 2:
                nodes.popleft()
        i += 1
    return head


def create_BST(arr: List[int]) -> Optional[BiTreeNode]:
    if not arr:
        return
    head = BiTreeNode(arr[0])
    for i in arr[1:]:
        par = temp = head
        if i > temp.val:
            temp = temp.right
        else:
            temp = temp.left
        while temp:
            par = temp
            if i > temp.val:
                temp = temp.right
            else:
                temp = temp.left
        if i > par.val:
            par.right = BiTreeNode(i)
        else:
            par.left = BiTreeNode(i)
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
