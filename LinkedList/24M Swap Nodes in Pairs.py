# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummynode = ListNode(0)
        pre = dummynode
        pre.next = head
        while pre.next and pre.next.next:
            # 1-2-3-4 翻转 2-1, 成为2-1-3-4，后转3-4变成4-3.
            # 但是，1 需要从1-3变成1-4
            # 因此，需要一个额外的指针记录1的地址，这样才能实现.next = 4
            # 因此，用.next记录翻转后的数，并用指针记录1的地址
            cur = pre.next  # 1
            future = pre.next.next  # 2
            cur.next = future.next  # 1-3
            future.next = cur  # 2-1
            pre.next = future  # 2
            pre = cur  # 1
        return dummynode.next







s = Solution()
phead = ListNode(1)
phead.next = ListNode(2)
phead.next.next = ListNode(3)
phead.next.next.next = ListNode(4)
test = s.swapPairs(phead)
while test:
    print(test.val)
    test = test.next
