# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        pointer = head
        while pointer:
            pointer.next, prev, pointer = prev, pointer, pointer.next
        return prev


s = Solution()
lhead = ListNode(1)
lhead.next = ListNode(2)
lhead.next.next = ListNode(3)
lhead.next.next.next = ListNode(4)
lhead.next.next.next.next = ListNode(5)
goal_head = s.reverseList(lhead)
while goal_head:
    print(goal_head.val)
    goal_head = goal_head.next