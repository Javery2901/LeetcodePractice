# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # two pointers to find the middle, reverse the right part, then compare
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy
        count = 0
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            count += 1
        # now we find the middle, if the number of list is odd, slow is sitting right at the middle
        # if the number of list is even, slow is sitting one before the middle
        # so we are reversing starting from slow.next
        prev, cur = slow, slow.next
        while cur:
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
        # prev is the last node now, we can start to check now
        first = head
        for _ in range(count):
            if first.val != prev.val:
                return False
            else:
                first = first.next
                prev = prev.next
        return True


