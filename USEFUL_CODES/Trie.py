class TreeNode:
    def __init__(self, x):
        self.val = x
        self.children = dict()
        self.isParent = False
        self.isEnd = False

    def __repr__(self):
        return self.val

    def __str__(self):
        return str(self.__repr__())


class Trie:

    def __init__(self):
        self.head = TreeNode(None)

    def insert(self, word: str) -> None:
        temp = self.head
        for i in word:
            if i not in temp.children:
                t1 = TreeNode(i)
                temp.children[i] = t1
                temp.isParent = True if len(temp.children) else False
                temp = t1
            else:
                temp.isParent = True if len(temp.children) else False
                temp = temp.children[i]
        temp.isEnd = True
        temp.isParent = True if len(temp.children) else False

    def search(self, word: str) -> bool:
        temp = self.head
        for i in word:
            if i not in temp.children:
                return False
            else:
                temp = temp.children[i]
        return True if temp.isEnd else False

    def startsWith(self, prefix: str) -> bool:
        temp = self.head
        for i in prefix:
            if i not in temp.children:
                return False
            else:
                temp = temp.children[i]
        return True
