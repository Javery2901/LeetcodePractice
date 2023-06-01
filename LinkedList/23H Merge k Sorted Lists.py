# Definition for singly-linked list.
from typing import Optional, List
from heapq import heappush, heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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



