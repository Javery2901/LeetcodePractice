# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        adict = {}
        dummy_node = ListNode()
        dummy_node.next = head
        pointer = dummy_node  # 0
        count = 0
        adict[count] = (pointer, pointer.next)  #{0: (0, 1)}
        while pointer.next:
            pointer = pointer.next
            count += 1
            adict[count] = (pointer, pointer.next)  # last: 5: (5, None)
        k = count - n + 1  # if n == 1:
        if n == 1:
            adict[k-1][0]. next = None
        elif n == count:
            dummy_node.next = head.next
        else:
            adict[k - 1][0].next = adict[k + 1][0]
        return dummy_node.next


s = Solution()
phead = ListNode(1)
phead.next = ListNode(2)
# phead.next.next = ListNode(3)
# phead.next.next.next = ListNode(4)
# phead.next.next.next.next = ListNode(5)
test = s.removeNthFromEnd(phead, 1)
while test:
    print(test.val)
    test = test.next
