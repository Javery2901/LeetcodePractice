# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def get_mid(node):
            slow, fast = head, head.next
            while fast and fast.next:
                slow, fast = slow.next, fast.next.next
            return slow

        def merge(list1, list2):
            new_head = tail = ListNode()
            while list1 and list2:
                if list1.val > list2.val:
                    tail.next = list2
                    list2 = list2.next
                else:
                    tail.next = list1
                    list1 = list1.next
                tail = tail.next
            if list1:
                tail.next = list1
            else:
                tail.next = list2
            return new_head.next

        if not head or not head.next:
            return head
        left = head
        right = get_mid(head)
        temp = right.next
        right.next = None
        right = temp

        left = self.sortList(left)
        right = self.sortList(right)

        return merge(left, right)
