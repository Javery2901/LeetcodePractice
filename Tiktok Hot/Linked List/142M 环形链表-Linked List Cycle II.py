# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        while True:
            if fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    break
            else:
                return
        # now they met in the loop now
        fast = dummy
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
