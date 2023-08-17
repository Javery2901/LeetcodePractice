# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # count the number of node first
        dummy = ListNode()
        dummy.next = head
        counter = dummy
        count = 0
        while counter.next:
            count += 1
            counter = counter.next

        left = dummy
        # need two more pointer, left and right to record the leftmost and rightmost

        while count >= k:
            prev, curr = left, left.next
            right = left.next

            for _ in range(k):
                # temp = curr.next
                # curr.next = prev
                # prev = curr
                # curr = temp
                curr.next, prev, curr = prev, curr, curr.next

            left.next.next = curr
            left.next = prev
            left = right  # dont forget this one

            count -= k
        return dummy.next
