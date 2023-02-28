# https://leetcode.com/problems/reverse-linked-list/
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def createList(array) -> Optional[ListNode]:
        if not len(array):
            return None
        ans = ListNode(array[0])
        temp = ans
        for i in array[1:]:
            temp.next = ListNode(i)
            temp = temp.next
        return ans

    # hacky solution
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        ans = []
        while head is not None:
            ans.append(head.val)
            head = head.next
        return self.createList(ans[::-1])

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


S = Solution()
