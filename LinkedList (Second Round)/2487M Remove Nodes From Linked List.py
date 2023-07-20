# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse the whole list

        def reverse(head):
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev, curr = curr, temp
            return prev

        start = current = reverse(head)
        while current:
            while current.next and current.val > current.next.val:
                current.next = current.next.next
            if not current.next:
                break
            else:
                current = current.next
        # current is the first node now
        # reverse again
        return reverse(start)

