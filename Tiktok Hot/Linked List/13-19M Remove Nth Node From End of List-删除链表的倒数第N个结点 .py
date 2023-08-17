# Definition for singly-linked list.
from typing import Optional
"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointers, fast and slow
        # let fast go n + 1 steps first, and then fast and slow go at the same time with the same step
        # when fast is at the tail, slow will be at the prev_node of deleting node
        # use dummy so that if the deleting node is the head
        dummy = ListNode()
        dummy.next = head
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        if n == 1:
            slow.next = None
        else:
            slow.next = slow.next.next
        return dummy.next
