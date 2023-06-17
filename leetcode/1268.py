# https://leetcode.com/problems/search-suggestions-system/
from USEFUL_CODES.LC import *


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for i in products:
            trie.add(i)

        def suggest(head: TreeNode) -> List[str]:
            if not head.children.values():
                return head.val
            lans = [head.val] if head.isEnd else []
            for j in head.children.values():
                for m in suggest(j):
                    lans.append(head.val + m)
            return lans

        cur_head = trie.head
        ans = []
        for i in range(len(searchWord)):
            if searchWord[i] in cur_head.children:
                cur_head = cur_head.children[searchWord[i]]
                if i == 0:
                    ans.append(list(sorted(suggest(cur_head)))[:3])
                else:
                    temp = []
                    for k in suggest(cur_head):
                        temp.append(searchWord[:i] + k)
                    ans.append(list(sorted(temp)[:3]))
            else:
                break
        ans += [[]] * (len(searchWord) - len(ans))
        return ans


S = Solution()
X = S.suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse")
print(X)
