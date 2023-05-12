# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        i = self
        while i is not None:
            yield i
            i = i.next

    def __next__(self):
        if self.next is None:
            raise StopIteration
        else:
            return self.next

    def __repr__(self):
        return str(self.val)


class Solution:
    def getSize(self, head) -> int:
        i = head
        n = 1
        while i is not None:
            n += 1
            i = i.next
        return n

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = self.getSize(head)
        j = s - n
        print(s, j)
        i = head
        while j != 0:
            i = i.next
            j -= 1
        return head


def visualise(head):
    ans = []
    i = head
    while i is not None:
        ans.append(i.val)
        i = i.next
    return ans


y = ListNode(2, None)
x = ListNode(1, y)
it = list(x)
print(it)
