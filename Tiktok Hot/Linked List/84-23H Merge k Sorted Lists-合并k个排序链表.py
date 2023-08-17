# Definition for singly-linked list.
import collections
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # combine one by one
        res = []
        if not lists:
            return res

        def connect(node1, node2):
            dummy = ListNode()
            curr = dummy
            while node1 and node2:
                if node1.val <= node2.val:
                    curr.next = node1
                    node1 = node1.next
                else:
                    curr.next = node2
                    node2 = node2.next
                curr = curr.next
            if node1:
                curr.next = node1
            else:
                curr.next = node2
            return dummy.next

        ls = collections.deque(lists)
        while len(ls) > 1:
            node1 = ls.popleft()
            node2 = ls.popleft()
            ls.append(connect(node1, node2))

    def mergeKLists_heapq(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = []
        for index, node in enumerate(lists):
            if node:
                heapq.heappush(hq, (node.val, index, node))

        dummy = ListNode()
        curr = dummy
        while hq:
            value, index, node = heapq.heappop(hq)
            if node.next:
                heapq.heappush(hq, (node.next.val, index, node.next))
            curr.next = node
            curr = curr.next
        return dummy.next
