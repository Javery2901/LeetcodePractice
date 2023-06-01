# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        pointer = dummy_node
        while list1 and list2:
            if list1.val <= list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next
        if list1:
            pointer.next = list1
        if list2:
            pointer.next = list2
        return dummy_node.next


s = Solution()
list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)
list2 = ListNode(2)
list2.next = ListNode(4)
list2.next.next = ListNode(6)
goal_head = s.mergeTwoLists(list1, list2)
while goal_head:
    print(goal_head.val)
    goal_head = goal_head.next
