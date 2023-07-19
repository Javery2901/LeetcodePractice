# Definition for a Node.
from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        adict = {}
        if not head:
            return head
        # 接下来head必不为空
        cur = head
        while cur:
            new_node = Node(cur.val)
            adict[cur] = new_node
            cur = cur.next
        # 处理next和random指针
        cur = head
        while cur:
            if cur.next:
                adict[cur].next = adict[cur.next]
            if cur.random:
                adict[cur].random = adict[cur.random]
            cur = cur.next
        return adict[head]



