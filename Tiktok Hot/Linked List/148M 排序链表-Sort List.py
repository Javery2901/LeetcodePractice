# Definition for singly-linked list.
from typing import Optional
"""
Given the head of a linked list, return the list after sorting it in ascending order.

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left = head
        right = self.get_mid(head)
        temp = right.next
        right.next = None
        right = temp

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

    def get_mid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow

    def merge(self, list1, list2):
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

    def sortList3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # The midpoint of the linked list is slow.next
        mid = slow.next
        # Set slow.next to None to separate the left and right halves of the linked list
        slow.next = None

        # Recursively sort the left and right halves of the linked list
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the two sorted halves of the linked list
        dummy = ListNode(0)
        curr = dummy
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        # Append the remaining nodes of the left or right half to the end of the sorted list
        curr.next = left or right

        return dummy.next

    def sortList2(self, head: Optional[ListNode]) -> Optional[ListNode]:  # 直接换值
        arr, itr = [], head
        while itr:
            arr.append(itr.val)
            itr = itr.next
        arr.sort()
        itr, i = head, 0

        while itr:
            itr.val = arr[i]
            i += 1
            itr = itr.next
        return head
