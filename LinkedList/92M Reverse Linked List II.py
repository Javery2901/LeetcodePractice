# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return
        dummy = ListNode()
        dummy.next = head
        pointer = dummy
        for _ in range(left - 1):
            pointer = pointer.next  # pointer is pointing to 1
        prev = None
        curr = pointer
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp  # prev is pointing 3, curr is pointing to 4
        # now link 2 to 5, 2 is pointer.next
        pointer.next.next = curr.next
        # now link 1 to 4, 1 is pointer
        pointer.next = curr
        return dummy.next


