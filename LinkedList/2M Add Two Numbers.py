# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0)
        cur = node
        base = 0
        while l1 and l2:
            cur.next = ListNode(0)
            cur = cur.next
            if (l1.val + l2.val) + base >= 10:
                cur.val = (l1.val + l2.val) + base - 10
                base = 1
            else:
                cur.val = (l1.val + l2.val) + base
                base = 0
            l1, l2 = l1.next, l2.next
        while l1:
            cur.next = ListNode(0)
            cur = cur.next
            if l1.val + base >= 10:
                cur.val = l1.val + base - 10
                base = 1
            else:
                cur.val = l1.val + base
                base = 0
            l1 = l1.next
        while l2:
            cur.next = ListNode(0)
            cur = cur.next
            if l2.val + base >= 10:
                cur.val = l2.val + base - 10
                base = 1
            else:
                cur.val = l2.val + base
                base = 0
            l2 = l2.next
        if base == 1:
            cur.next = ListNode(1)
        return node.next


l1 = ListNode(5)
l1.next = ListNode(3)
l1.next.next = ListNode(5)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
s= Solution()
goal_node = s.addTwoNumbers(l1, l2)
while goal_node:
    print(goal_node.val)
    goal_node = goal_node.next
