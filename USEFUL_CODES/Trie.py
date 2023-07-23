from typing import Dict, Optional


class TreeNode:
    """
    A node in a Trie data structure.
    """

    def __init__(self, x: Optional[str | bytes | int]) -> None:
        self.val: Optional[str | bytes | int] = x
        self.children: Dict[str | bytes | int, TreeNode] = dict()
        self.is_parent: bool = False
        self.is_end: bool = False

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.val)

    def __contains__(self, item):
        return item in self.children

    def __getitem__(self, item):
        return self.children[item]

class Trie:
    """
    A Trie data structure.
    """

    def __init__(self) -> None:
        self.head: TreeNode = TreeNode(None)

    def __bool__(self) -> bool:
        return len(self.head.children) > 0

    def add(self, word: str | bytes) -> None:
        """
        Add a word to the Trie, by calling insert

        :param word: The word to add.
        :return: None.
        """
        return self.insert(word)

    def insert(self, word: str | bytes) -> None:
        """
        Insert a word into the Trie.

        :param word: The word to insert.
        :return: None.
        """
        temp = self.head
        for i in word:
            if i not in temp.children:
                t1 = TreeNode(i)
                temp.children[i] = t1
                temp.is_parent = True if len(temp.children) else False
                temp = t1
            else:
                temp.is_parent = True if len(temp.children) else False
                temp = temp.children[i]
        temp.is_end = True
        temp.is_parent = True if len(temp.children) else False

    def search(self, word: str | bytes) -> bool:
        """
        Search for a word in the Trie.

        Example:

        my_trie = Trie()

        my_trie.add("test_case")

        my_trie.search("test")  # reruns False

        my_trie.search("test_case")  # reruns True

        :param word: The word to search for.
        :return: True if the word is found, False otherwise.
        """
        temp = self.head
        for i in word:
            if i not in temp.children:
                return False
            else:
                temp = temp.children[i]
        return temp.is_end

    def starts_with(self, prefix: str | bytes) -> bool:
        """
        Check if any word in the Trie starts with the given prefix.


        Example:

        my_trie = Trie()

        my_trie.add("test_case")

        my_trie.starts_with("test")  # reruns True

        my_trie.search("test")  # when search would return False

        :param prefix: The prefix to check.
        :return: True if there is a word starting with the prefix,
                False otherwise.
        """
        temp = self.head
        for i in prefix:
            if i not in temp.children:
                return False
            else:
                temp = temp.children[i]
        return True

    def remove(self, word: str | bytes) -> bool:
        """
        Remove a word from the Trie.

        my_trie = Trie()

        my_trie.add("test_case")

        my_trie.remove("test_case")  # when search would return False

        my_trie.starts_with("test")  # reruns False as it was removed


        :param word: The word to remove.
        :return: True if the word was successfully removed,
        False otherwise.
        """
        if not self.search(word):
            return False
        nodes = [self.head]
        for i in word:
            nodes.append(nodes[-1].children[i])
        if nodes[-1].is_parent:
            nodes[-1].is_end = False
            return True
        while nodes:
            item = nodes.pop()
            if item.val is None:
                return True
            if nodes[-1].is_parent:
                nodes[-1].children.pop(item.val)
                if nodes[-1].is_end or len(nodes[-1].children):
                    return True
        return False
