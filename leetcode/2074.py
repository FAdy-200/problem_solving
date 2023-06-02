# https://leetcode.com/problems/reverse-nodes-in-even-length-groups/
from USEFUL_CODES.LinkedList import *
from typing import Tuple
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        groups:List[List[Optional[ListNode]]] = []
        m = k = 0
        temp = head
        while head:
            if not k:
                groups.append([head,temp])
                m += 1
                k = m
            temp = head
            head = head.next
            k-=1
        for i in range(2,len(groups)+1):
            even = not i%2
            if i == len(groups):
                if not (i-k)%2:
                    even = True
                elif even:
                    break
            if even:
                curr ,prev = groups[i-1][0], None
                counter = i
                while counter and curr:
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
                    counter -= 1
                if not i%2:
                    groups[i - 1][1].next = prev
                else:
                    groups[i - 2][0].next = prev
            else:
                groups[i - 2][0].next = groups[i - 1][0]
        return groups[0][0]





S = Solution()
X = S.reverseEvenLengthGroups(create_linked_list([4,3,0,5,1,2,7,8,6]))
print(X)