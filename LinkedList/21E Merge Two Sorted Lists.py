# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        output = dummy
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                output.next = curr1
                curr1 = curr1.next
            else:
                output.next = curr2
                curr2 = curr2.next
            output = output.next

        while curr1:
            output.next = curr1
            break

        while curr2:
            output.next = curr2
            break

        return output.next


s = Solution()
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

merge = s.mergeTwoLists(list1, list2)
while merge:
    print(merge.val, end=' ')
    merge = merge.next

