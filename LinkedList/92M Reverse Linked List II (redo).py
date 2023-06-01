# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        pointer = dummy_node
        for _ in range(left - 1):
            pointer = pointer.next
            # pointer = 1
        prev = None
        cur = pointer.next
        for _ in range(right - left + 1):
            cur.next, prev, cur = prev, cur, cur.next
            # 2 3 4 -> 4 3 2
            # cur = 5, prev = 4
        print(pointer.val, pointer.next.val, pointer.next.next)
        pointer.next.next = cur
        pointer.next = prev
        return dummy_node.next

s = Solution()
phead = ListNode(1)
phead.next = ListNode(2)
phead.next.next = ListNode(3)
phead.next.next.next = ListNode(4)
phead.next.next.next.next = ListNode(5)
test = s.reverseBetween(phead, 2, 4)
while test:
    print(test.val)
    test = test.next

