# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        address = set()
        pointer = head
        while pointer:
            if pointer not in address:
                address.add(pointer)
            else:
                return True
            pointer = pointer.next
        return False
