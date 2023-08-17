# Definition for singly-linked list.
from typing import Optional
'''
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        dummy = ListNode(-101, head)
        prev, curr = dummy, head
        while curr and curr.next:
            if curr.val != curr.next.val:
                prev = prev.next
                curr = curr.next
            else:
                while curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
                curr = curr.next
        return dummy.next
