# https://leetcode.com/problems/word-search-ii/
from typing import *
from USEFUL_CODES.Trie import *


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str] | Set[str]:
        n = len(board)
        m = len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
        to_check = set()
        for i, row in enumerate(board):
            for j, let in enumerate(row):
                if let in trie.head.children:
                    to_check.add((i, j))
        moves = [-1, 0, 1]

        def dfs(li: int, lj: int, th: TreeNode, visited: set) -> List[str]:
            visited.add((li, lj))
            if not th:
                return []
            Lans = []
            if th.isEnd:
                if not th.isParent:
                    return [board[li][lj]]
                Lans.append(board[li][lj])
            for ti in moves:
                for tj in moves:
                    if ti == tj or (ti != 0 and tj != 0):
                        continue
                    if n > li + ti >= 0 and m > lj + tj >= 0 and (li + ti, lj + tj) not in visited:
                        if board[li + ti][lj + tj] in th.children:
                            for item in dfs(li + ti, lj + tj, th.children[board[li + ti][lj + tj]], visited.copy()):
                                Lans.append(board[li][lj] + item)
            return Lans

        ans = set()
        for i in to_check:
            if board[i[0]][i[1]] in trie.head.children:
                for sol in dfs(i[0], i[1], trie.head.children[board[i[0]][i[1]]], set()):
                    if sol:
                        ans.add(sol)
                        trie.remove(sol)
        return ans


S = Solution()
X = S.findWords(board=
                [["a","a"]],
                words=
                ["a"])
print(X)
