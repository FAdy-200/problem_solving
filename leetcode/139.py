# https://leetcode.com/problems/word-break/
from typing import *
from USEFULL_CODES.Trie import Trie, TreeNode


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        my_trie = Trie()
        for c in wordDict:
            my_trie.insert(c)
        d = {}

        def mySearch(i: int, node: TreeNode):
            if i in d:
                return d[i]
            for j in range(i, len(s)):
                if s[j] not in node.children:
                    d[i] = False
                    return False
                else:
                    if node.children[s[j]].isParent and node.children[s[j]].isEnd:
                        if mySearch(j + 1, node.children[s[j]]):
                            d[i] = True
                            return True
                        node = my_trie.head
                        continue
                    elif node.children[s[j]].isEnd:
                        node = my_trie.head
                        continue
                    node = node.children[s[j]]
            d[i] = True if not node.val or node.isEnd else False
            return d[i]

        return mySearch(0, my_trie.head)


S = Solution()
X = S.wordBreak(s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", wordDict=["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"])
print(X)
