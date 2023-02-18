from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Dll:
    def __init__(self):
        self.first = None
        self.last = None

    def delete(self):
        if self.first is not self.last:
            of = self.first
            nf = self.first.right
            nf.left = None
            self.first = nf
            return of.val
        else:
            n = self.first
            self.last = None
            self.first = None
            return n.val

    def moveToLast(self, node):
        if node is not self.first and node is not self.last:
            node.left.right = node.right
            node.right.left = node.left
            self.last.right = node
            node.left = self.last
            node.right = None
            self.last = node
        elif node is self.first and node is not self.last:
            self.first = self.first.right
            self.first.left = None
            self.last.right = node
            node.left = self.last
            node.right = None
            self.last = node
        else:
            return

    def insert(self, node):
        if self.last is None:
            self.last = node
            self.first = node
        else:
            self.last.right = node
            node.left = self.last
            self.last = node


class LRUCache:

    def __init__(self, capacity: int):
        self.data = [[-1,-1]]*3001
        self.size = 0
        self.capacity = capacity
        self.dll = Dll()

    def get(self, key: int) -> int:
        ss = self.data[key]
        if ss != [-1, -1]:
            if ss[0] != -1:
                self.dll.moveToLast(ss[1])
            return ss[0]
        return -1

    def put(self, key: int, value: int) -> None:
        ss = self.data[key]
        if ss != [-1, -1]:
            if ss[0] != -1:
                self.dll.moveToLast(ss[1])
            else:
                node = Node(value)
                self.dll.insert(node)
                self.data[key][1] = node
            self.data[key][0] = value
            return
        if self.size == self.capacity:
            n = self.dll.delete()
            self.data[n] = [-1, -1]
            node = Node(key)
            self.dll.insert(node)
            self.data[key] = [value, node]
        else:
            self.size += 1
            node = Node(key)
            self.dll.insert(node)
            self.data[key] = [value, node]


# x = ["put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
#      "get", "put", "get",
#      "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get", "put", "get", "get",
#      "get", "put", "put",
#      "put", "get", "put", "get", "get", "put", "put", "get", "put", "put", "put", "put", "get", "put", "put", "get",
#      "put", "put", "get",
#      "put", "put", "put", "put", "put", "get", "put", "put", "get", "put", "get", "get", "get", "put", "get", "get",
#      "put", "put", "put",
#      "put", "get", "put", "put", "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put",
#      "get", "put", "put",
#      "put", "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
# z = [[10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
#      [1, 30], [11], [9, 12], [7], [5], [8]
#     , [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11], [8], [2, 14], [1], [5], [4], [11, 4],
#      [12, 24], [5, 18], [13], [7, 23],
#      [8], [12], [3, 27], [2, 12], [5], [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12],
#      [10], [4, 15], [7, 22], [11, 26]
#     , [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28],
#      [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12],
#      [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1],
#      [2, 2], [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]


# obj = LRUCache(10)
#
# for i in range(len(z)):
#     if x[i] == "put":
#         obj.put(z[i][0], z[i][1])
#     else:
#         if z[i][0] == 12:
#             ffgg = 0
#         obj.get(z[i][0])


class LRUCacheE:

    def __init__(self, capacity: int):
        self.data = [-1] * 3001
        self.size = 0
        self.capacity = capacity
        self.order = []

    def get(self, key: int) -> int:
        an = self.data[key]
        if an != -1:
            self.order.remove(key)
            self.order.append(key)
        return an

    def put(self, key: int, value: int) -> None:
        if self.data[key] != -1:
            self.data[key] = value
            self.order.remove(key)
            self.order.append(key)
            return
        if self.capacity == self.size:
            k = self.order.pop(0)
            self.data[k] = -1
            self.data[key] = value
            self.order.append(key)
        else:
            self.size += 1
            self.order.append(key)
            self.data[key] = value

obj = LRUCacheE(3)
obj.put(1, 1)
obj.put(2, 2)
obj.put(3, 3)
obj.put(4, 4)
obj.get(4)
obj.get(3)
obj.get(2)
obj.get(1)
obj.put(5, 5)
obj.get(1)
obj.get(2)
obj.get(3)
obj.get(4)
obj.get(5)
