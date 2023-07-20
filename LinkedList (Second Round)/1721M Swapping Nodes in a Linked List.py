# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        # two pointers, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 k = 2
        # first_pointer points to 1, second_pointer points to 6
        # then relink
        first, second = dummy, dummy
        for _ in range(k):
            first = first.next
        pointer = first
        while pointer:
            second, pointer = second.next, pointer.next
        # now first is -> 2, second is -> 6
        first.val, second.val = second.val, first.val
        return dummy.next



