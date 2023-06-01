# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            # curr.next, prev, curr = prev, curr, curr.next
        return prev


s = Solution()
pHead = ListNode(1)
pHead.next = ListNode(2)
pHead.next.next = ListNode(3)
reversed_head = s.reverseList(pHead)
while reversed_head:
    print(reversed_head.val)
    reversed_head = reversed_head.next
