# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        dummy_node.next = head
        pointer = dummy_node
        for _ in range(left - 1):
            pointer = pointer.next
        prev = None
        cur = pointer.next  # cur = 2
        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            # last: cur = 5
        pointer.next.next = cur
        pointer.next = prev
        return dummy_node.next


s = Solution()
phead = ListNode(5)
phead.next = ListNode(2)
# phead.next.next = ListNode(3)
# phead.next.next.next = ListNode(4)
# phead.next.next.next.next = ListNode(5)
test = s.reverseBetween(phead, 1, 2)
while test:
    print(test.val)
    test = test.next


