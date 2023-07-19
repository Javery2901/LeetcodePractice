class ListNode:

    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        i = 0
        while i < index:
            curr = curr.next
            i += 1
        if curr:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode()
        new_node.val = val
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
        return

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
        else:
            new_node = ListNode()
            new_node.val = val
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return
        if index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            i = 0
            while i < index:
                curr = curr.next
                i += 1
            new_node = ListNode()
            new_node.val = val
            curr.prev.next = new_node
            new_node.prev = curr.prev
            curr.prev = new_node
            new_node.next = curr
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        curr = self.head
        i = 0
        while i < index:
            curr = curr.next
            i += 1
        # curr will be deleted
        if curr == self.head:
            self.head = self.head.next
        elif curr == self.tail:
            self.tail = self.tail.prev
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
obj.addAtHead(1)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
obj.deleteAtIndex(0)
