from typing import List, Any, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()


def create_linked_list(arr: List[Any]) -> Optional[ListNode]:
    if not arr:
        return None

    head = ListNode(arr[0])
    tmp = head

    for i in arr[1:]:
        tmp.next = ListNode(i)
        tmp = tmp.next

    return head
