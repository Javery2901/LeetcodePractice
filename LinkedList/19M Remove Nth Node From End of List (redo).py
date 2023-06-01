# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        cur = head
        while cur:
            i += 1
            cur = cur.next
        # i: the numbers of whole sll

        index = i - n + 1  # this node will be removed
        i = 1
        cur = head
        prev = None
        while i != index and cur:
            i += 1
            prev = cur
            cur = cur.next
        if prev:
            prev.next = cur.next
        else:
            head = cur.next
        # print(prev.val)
        # print(prev.next.val)
        return head


lhead = ListNode(1)
# lhead.next = ListNode(2)
# lhead.next.next = ListNode(3)
# lhead.next.next.next = ListNode(4)
# lhead.next.next.next.next = ListNode(5)
s = Solution()
# s.removeNthFromEnd(lhead, 2)
goal_head = s.removeNthFromEnd(lhead, 1)
while goal_head:
    print(goal_head.val)
    goal_head = goal_head.next
