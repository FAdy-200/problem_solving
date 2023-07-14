# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/?envType=study-plan-v2&envId=leetcode-75
from USEFUL_CODES.LC import *


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        if length == 1:
            return None
        before_mid = length // 2 - 1
        temp = head
        while before_mid:
            temp = temp.next
            before_mid -= 1
        temp.next = temp.next.next
        return head
