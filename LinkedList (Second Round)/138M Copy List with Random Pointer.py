from cmath import inf


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        # use a dictionary to save the information of the original node and new node {original_node: new_node}
        # eg: {original_node(7): new_node(7)}
        dic = {}
        dummy = Node(-10001)
        orig = head
        curr = dummy
        while orig:
            curr.next = Node(orig.val)
            dic[orig] = curr.next  # create dictionary
            orig = orig.next
            curr = curr.next
        # The new linked list has done, now set random pointer using dictionary

        curr = dummy.next
        orig = head
        while orig:
            if orig.random:
                curr.random = dic[orig.random]
            orig = orig.next
            curr = curr.next
        return dummy.next

    def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
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




