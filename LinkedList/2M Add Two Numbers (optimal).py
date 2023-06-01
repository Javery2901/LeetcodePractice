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

        while l1 or l2 or base:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            summ = val1 + val2 + base
            base = summ // 10
            summ = summ % 10
            cur.next = ListNode(summ)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return node.next


l1 = ListNode(5)
l1.next = ListNode(3)
l1.next.next = ListNode(5)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
s = Solution()
goal_node = s.addTwoNumbers(l1, l2)
while goal_node:
    print(goal_node.val)
    goal_node = goal_node.next
