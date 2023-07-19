# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 类似于24M，24是每两个翻转一次，此题是每k个反转

        dummy_node = ListNode()
        checker = dummy_node
        checker.next = head
        if k <= 1:
            return head
        count = 0
        while checker.next:
            count += 1
            checker = checker.next

        left = dummy_node
        left.next = head

        while count >= k:  # start to loop: in the loop, every round from first to second, reverse
            prev = left  # prev: dummy_node,
            cur = left.next  # cur: 1,
            right = left.next  # right: 1,
            for _ in range(k):
                cur.next, prev, cur = prev, cur, cur.next
            #     print(cur.val, prev.val)
            # print(left.val)
            # 1 2 3 4 5 k = 3
            # start: cur = 1 , prev = dummy_node
            # end: cur = 4 , prev = 3
            left.next.next = cur  # 1 -> 4,
            left.next = prev  # dummy_node -> 4,
            left = right  # left: 1

            count -= k
        return dummy_node.next

s = Solution()
lhead = ListNode(1)
lhead.next = ListNode(2)
lhead.next.next = ListNode(3)
lhead.next.next.next = ListNode(4)
lhead.next.next.next.next = ListNode(5)
goal_head = s.reverseKGroup(lhead, 3)
while goal_head:
    print(goal_head.val)
    goal_head = goal_head.next


