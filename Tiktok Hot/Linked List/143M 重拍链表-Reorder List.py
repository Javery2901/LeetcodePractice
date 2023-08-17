# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle node first
        # reverse the right part of linked list
        # then starting from head, insert node one by one
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # slow is the middle node, reverse the right part now
        prev, cur = None, slow
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        # prev is the last node, reorganize the linked list now
        first, second = head, prev

        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next


