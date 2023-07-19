# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        # 1 2 3 4 5, fast = 5, slow = 3
        prev, cur = None, mid  # reverse second half: 5 - 4 - 3
        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        head_of_second_rev = prev  # 5
        first, second = head, head_of_second_rev  # first = 1, second = 4

        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next


s = Solution()
phead = ListNode(1)
phead.next = ListNode(2)
phead.next.next = ListNode(3)
phead.next.next.next = ListNode(4)
phead.next.next.next.next = ListNode(5)

test = s.reorderList(phead)
# while test:
#     print(test.val)
#     test = test.next
print(phead.val)
print(phead.next.val)
print(phead.next.next.val)
print(phead.next.next.next.val)
print(phead.next.next.next.next.val)

