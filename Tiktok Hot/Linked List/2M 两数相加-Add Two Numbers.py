# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        base = 0
        current = dummy

        while l1 or l2 or base:  # or base is important
            add_sum = base
            if l1:
                add_sum += l1.val
                l1 = l1.next
            if l2:
                add_sum += l2.val
                l2 = l2.next
            base = add_sum // 10
            add_sum = add_sum % 10
            current.next = ListNode(add_sum)
            current = current.next
        return dummy.next


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
