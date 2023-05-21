# https://leetcode.com/problems/reverse-nodes-in-k-group/

from typing import *
from USEFUL_CODES.LinkedList import *


# TODO: finish this
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        thead = head
        while thead:
            n += 1
            thead = thead.next

        lists = [[] for _ in range(n // k + 1)]
        thead = head
        i = 0
        j = 0
        while thead:
            if i == 0:
                lists[j].append(thead)
            if i == k - 1:
                lists[j].append(thead)
                i = -1
                j += 1
            thead = thead.next
            i += 1
        ans = lists[0][0]
        for ind, item in enumerate(lists):
            if len(item) != 2:
                if ind:
                    lists[ind - 1][0].next = item[0]
                    continue
            prev, curr = None, item[0]
            i = 0
            while i < k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                i += 1
            if ind:
                lists[ind-1][0].next = item[1]
            else:
                ans = item[1]
        return ans


S = Solution()
LL = create_linked_list([1, 2, 3, 4, 5,6,7])
X = S.reverseKGroup(LL, 3)
print(X)
