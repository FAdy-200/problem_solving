# https://leetcode.com/problems/merge-two-sorted-lists/description/
from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    inf = float("inf")

    # yes i am lazy lol
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeKLists([list1, list2])

    @staticmethod
    def getMin(lists: List[Optional[ListNode]]):
        gi, gj = 0, Solution.inf
        for i, j in enumerate(lists):
            if j:
                if j.val < gj:
                    gi = i
                    gj = j.val
        return gi, gj

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists):
            ans = ListNode()
            head = ans
            i = self.getMin(lists)
            temp = ans
            if i[1] == Solution.inf:
                return None
            while i[1] != Solution.inf:
                ans.val = i[1]
                lists[i[0]] = lists[i[0]].next
                ans.next = ListNode()
                temp = ans
                ans = ans.next
                i = self.getMin(lists)
            temp.next = None
            return head
        return None
