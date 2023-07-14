# https://leetcode.com/problems/odd-even-linked-list/?envType=study-plan-v2&envId=leetcode-75
from USEFUL_CODES.LC import *


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        for i in range(2):
            if not temp:
                return head
            temp = temp.next
        first_even = head.next
        curr_even = first_even
        curr_odd = head
        old_odd = head
        while curr_even and curr_odd:
            curr_odd.next = curr_even.next
            old_odd = curr_odd
            curr_odd = curr_odd.next
            if curr_odd:
                curr_even.next = curr_odd.next
                curr_even = curr_even.next
        if curr_odd:
            curr_odd.next = first_even
        else:
            old_odd.next = first_even
        return head

S = Solution()
LL = create_linked_list([1,2,3,4,5,6,7,8])
X = S.oddEvenList(LL)
print(X)
