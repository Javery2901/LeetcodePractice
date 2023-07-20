# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        return prev

    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def recursive(prev, curr):
            if not curr:
                return prev
            temp = curr.next
            curr.next = prev
            return recursive(curr, temp)

        return recursive(None, head)