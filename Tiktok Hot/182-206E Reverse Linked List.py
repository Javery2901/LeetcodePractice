# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def reverseList_it(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def recursion(prev, curr):
            if not curr:
                return
            temp = curr.next
            curr.next = prev
            return recursion(curr, temp)

        return recursion(None, head)

