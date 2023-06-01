# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy_node = ListNode(0, head)
        if not head:
            return head
        prev = head
        cur = head.next
        # print(prev.val, cur.val)
        while cur:
            if cur.val == prev.val:
                cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next
        return head


lhead = ListNode(1)
lhead.next = ListNode(1)
lhead.next.next = ListNode(1)
lhead.next.next.next = ListNode(2)
# lhead.next.next.next.next = ListNode(3)
s = Solution()
goal_head = s.deleteDuplicates(lhead)
while goal_head:
    print(goal_head.val)
    goal_head = goal_head.next


