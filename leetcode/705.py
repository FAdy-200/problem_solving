# https://leetcode.com/problems/design-hashset/
class MyHashSet:

    def __init__(self):
        """
        Hash implementation using a 2d simple array implementation of size n,1000 where the n is dynamic and
        the lookup is done like:
        i, j = key // 1000, key % 1000
        ele = arr[i][j]
        """
        self.hs = []

    def add(self, key: int) -> None:
        i,j = key//1000 , key % 1000
        if i >= len(self.hs):
            for m in range(len(self.hs),i+1):
                self.hs.append([-1 for _ in range(1000)])
        self.hs[i][j] = key
    def remove(self, key: int) -> None:
        i, j = key // 1000, key % 1000
        if i < len(self.hs):
            self.hs[i][j] = -1

    def contains(self, key: int) -> bool:
        i, j = key // 1000, key % 1000
        if i >= len(self.hs):
            return False
        if self.hs[i][j] != -1:
            return True
        return False
# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1000000)
# obj.remove(key)
# param_3 = obj.contains(key)
