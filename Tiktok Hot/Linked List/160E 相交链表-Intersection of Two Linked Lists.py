# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_pointer = headA
        b_pointer = headB
        while a_pointer != b_pointer:
            # if no intersection, a_pointer and b_pointer will both be None
            if a_pointer:
                a_pointer = a_pointer.next
            else:
                a_pointer = headB
            if b_pointer:
                b_pointer = b_pointer.next
            else:
                b_pointer = headA
        return a_pointer