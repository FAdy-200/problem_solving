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

        for m in range(n // k):
            i = 0
            if not m:

                prev, curr = None, head
                while i < k:
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
                    if i == k-2:
                        last = prev
                    i += 1
                main_head = prev
            else:
                # prev, curr = None, head
                while i < k:
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
                    if i == k-2:
                        last = prev
                    i += 1

        return main_head


S = Solution()
LL = create_linked_list([1, 2, 3])
X = S.reverseKGroup(LL, 2)
print(X)
