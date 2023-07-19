# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # initialize two dummy node, one is leading to all node smaller than x
        # another is leading to all nodes bigger than or equal to x
        if not head:
            return
        dummy1 = ListNode()
        first = dummy1
        dummy2 = ListNode()
        second = dummy2
        while head:
            if head.val < x:
                first.next = head
                first = first.next
            else:
                second.next = head
                second = second.next
            head = head.next
        first.next = dummy2.next
        second.next = None  # this is important
        return dummy1.next

