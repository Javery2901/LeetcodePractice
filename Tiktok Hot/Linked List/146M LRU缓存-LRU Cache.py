import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.map:
            self.map.move_to_end(key, last=True)
            return self.map[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key] = value
            self.map.move_to_end(key, last=True)
            return
        if len(self.map) == self.capacity:
            self.map.popitem(last=False)
        self.map[key] = value

class Node:
    def __init__(self, key: int or None, val: int or None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.head = Node(None, None)  # head -> A -> B -> C -> D -> tail
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        node.prev.next = node
        node.next.prev = node

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            # we can simply update the key-value
            node = self.key_to_node[key]
            node.val = value
            self._remove(node)
            self._add(node)
            return
        if self.size < self.capacity:
            # insert the node to the last
            new_node = Node(key, value)
            self.key_to_node[key] = new_node
            self._add(new_node)
            self.size += 1
        else:
            # delete the head, and insert the node the last
            deleting_node = self.head.next
            self._remove(deleting_node)
            del self.key_to_node[deleting_node.key]

            new_node = Node(key, value)
            self.key_to_node[key] = new_node
            self._add(new_node)









# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
