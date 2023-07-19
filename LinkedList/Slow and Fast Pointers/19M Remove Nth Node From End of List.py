# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointers, fast and slow
        # let fast go n + 1 steps first, and then fast and slow go at the same time with the same step
        # when fast is at the tail, slow will be at the prev_node of deleting node
        # use dummy so that if the deleting node is the head
        dummy = ListNode()
        dummy.next = head
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
