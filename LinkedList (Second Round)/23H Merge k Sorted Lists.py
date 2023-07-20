# Definition for singly-linked list.
from collections import deque
from heapq import heappush, heappop
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # idae: combine the lists one by one
        if not lists:
            return

        def combine(node1, node2):
            dummy = ListNode()
            current = dummy
            while node1 and node2:
                if node1.val <= node2.val:
                    current.next = node1
                    node1 = node1.next
                else:
                    current.next = node2
                    node2 = node2.next
                current = current.next
            if node1:
                current.next = node1
            if node2:
                current.next = node2
            return dummy.next

        ls = deque(lists)
        while len(ls) > 1:
            node1 = ls.popleft()
            node2 = ls.popleft()
            lists.append(combine(node1, node2))
        return ls[0]

    def mergeKLists_heapq(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(hq, (lists[i].val, i))  # (node.val, ith in lists) k nodes
                lists[i] = lists[i].next

        dummy_node = ListNode()
        cur = dummy_node
        while hq:
            v, i = heappop(hq)
            cur.next = ListNode(v)
            cur = cur.next
            if lists[i]:
                heappush(hq, (lists[i].val, i))
                lists[i] = lists[i].next
        return dummy_node.next

