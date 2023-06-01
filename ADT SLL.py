class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def appendleft(self, data):
        node = Node(data)
        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            node.next = self.__head
            self.__head = node
        self.__size += 1

    def append(self, data):
        node = Node(data)
        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            self.__tail.next = node
            self.__tail = node
        self.__size += 1

    def appendmid(self, data, index):
        if index <= 0:
            self.appendleft(data)
        elif index >= self.__size:
            self.append(data)
        else:
            node = Node(data)
            cur = self.__head
            for _ in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def front(self):
        if self.__head is None:
            return
        return self.__head.data

    def back(self):
        if self.__head is None:
            return
        return self.__tail.data

    def popleft(self):
        if self.__head is None:
            return
        self.__head = self.__head.next
        if self.__head is None:
            self.__tail = None

    def empty(self):
        return self.__head is None

    def sllprint(self):
        cur = self.__head
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next


l = SLL()
l.appendleft(1)
print(l.front())
l.appendleft(2)
print(l.front())
l.appendleft(3)
print(l.front())
l.append(4)
print(l.back())
l.popleft()
print(l.front())
l.sllprint()