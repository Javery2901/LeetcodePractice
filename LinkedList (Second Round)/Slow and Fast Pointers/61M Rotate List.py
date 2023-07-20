# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        # iterate once to find the length
        length = 0
        dummy = ListNode(0, head)
        slow = dummy
        while slow.next:
            slow = slow.next
            length += 1

        # now we know the length, use two pointers to figure out where the rotating node is
        slow = fast = dummy
        k = k % length
        for _ in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next  # fast is the last node which should be linked to head
            slow = slow.next  # slow is the last node after rotation

        if not slow.next:
            return dummy.next  # if slow is the last node, nothing changed
        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None
        return dummy.next



