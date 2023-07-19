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
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            # 1 2 3 4 -> fast = 3, slow = 2
            # 1 2 3 4 5 -> fast = 5, slow = 3
            # slow is the middle one
            # fast is no use
        # print(fast.val, slow.val)

        # reverse the node from slow(mid) to the last
        # 1 2 3 4 -> 1 2, 4 3 2
        # 1 2 3 4 5 -> 1 2 3, 5 4 3
        mid = slow
        prev = None
        while mid.next:
            mid.next, prev, mid = prev, mid, mid.next
            # 3 4 5 None -> 5 4 3 None
            # at last: mid = 5, prev = 4
        mid.next = prev
        # print(mid.val, mid.next.val, mid.next.next.val, mid.next.next.next)

        first, second = head, mid
        while second.next:
            # temp1 = first.next
            # first.next = second
            # first = temp1
            #
            # temp2 = second.next
            # second.next = first
            # second = temp2
            first.next, first = second, first.next
            second.next, second = first, second.next


s = Solution()
phead = ListNode(1)
phead.next = ListNode(2)
phead.next.next = ListNode(3)
phead.next.next.next = ListNode(4)
phead.next.next.next.next = ListNode(5)
s.reorderList(phead)
while phead:
    print(phead.val)
    phead = phead.next



