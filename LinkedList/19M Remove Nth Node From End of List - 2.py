# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        # count : 5
        n_inorder = count - n + 1
        pre = None
        cur = head
        count1 = 1
        while cur:
            if count1 == n_inorder:
                if pre is None:
                    head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                count1 += 1
                pre = cur
                cur = cur.next
        return head


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
