# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 人为构造循环，A遍历后指向B
        ahead = headA
        bhead = headB
        while ahead != bhead:
            if ahead is None:
                ahead = headB
            else:
                ahead = ahead.next
            if bhead is None:
                bhead = headA
            else:
                bhead = bhead.next
        return ahead




