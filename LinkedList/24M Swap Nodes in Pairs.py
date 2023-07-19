# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        def recursive(head):
            if not head or not head.next:
                return head

            prev = head
            cur = head.next
            future = head.next.next

            cur.next = prev
            prev.next = recursive(future)
            return cur
        return recursive(head)

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 2 3 4 -> 2 1 3 4, 3 4 翻转时需要知道1的地址，
        # 即2 1 操作时需要额外一个指针来保存1，这样3 4 翻转后1的next可以链接3
        # 一般两个指针时： prev = None， cur = head
        # 三个指针时，新建一个node
        dummy_node = ListNode()
        pre = dummy_node
        pre.next = head
        while pre.next and pre.next.next:
            cur = pre.next
            future = pre.next.next # cur -> 1, future -> 2
            # 如果两个都存在，反转，如果只有一个cur，不操作
            cur.next = future.next  # 1 -> 3
            future.next = cur
            # dummy_node 要连到2上，
            pre.next = future
            pre = cur # 用pre保存1的地址
        return dummy_node.next