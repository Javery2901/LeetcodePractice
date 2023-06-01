# Definition for singly-linked list.
from collections import deque
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        def combine(l1, l2):
            dummy_node = ListNode()
            cur = dummy_node
            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next =l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1:
                cur.next = l1
            else:
                cur.next = l2
            return dummy_node.next
        ls = deque(lists)
        while len(ls) >= 2:
            l1 = ls.popleft()
            l2 = ls.popleft()
            ls.append(combine(l1, l2))
        return ls[0]




