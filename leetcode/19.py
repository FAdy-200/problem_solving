# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        sz = 0
        while temp:
            sz += 1
            temp = temp.next
        tbr = sz - n
        print(tbr)
        prev, cur = None, head
        for _ in range(tbr):
            prev = cur
            cur = cur.next
        if prev:
            prev.next = cur.next
        else:
            head = head.next
        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = head
        for _ in range(n):
            p2 = p2.next
        temp = p1
        while p2:
            temp = p1
            p1 = p1.next
            p2 = p2.next
        # print(f"{p1}\n{p2}\n{temp}")
        if temp.next and temp is not p1:
            temp.next = temp.next.next
        else:
            head = head.next
        return head
