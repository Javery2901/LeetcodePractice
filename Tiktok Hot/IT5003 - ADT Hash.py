class HashTable:  # try separate chaining
    def __init__(self):
        self.size = 97  # use a prime for the best performance
        self.table = [[] for _ in range(self.size)]  # [[(key, val), (key2, val2)], [(key3, val3)]]

    def hash_function(self, key):
        _sum = 0
        for char in key:
            _sum = ((_sum * 26) % self.size + (ord(char) - ord('A') + 1)) % self.size
            # very interesting function, this function makes sure that the result lives in [0, size]
            # assumption 1: key is ['A', 'B', 'C'.... 'Z']
            # assumption 2: key is short string
        return _sum

    def search(self, key):
        for k, v in self.table[self.hash_function(key)]:
            if k == key:
                return v
        return None

    def remove(self, key):
        row = self.table[self.hash_function(key)]
        for i in range(len(row)):
            if row[i][0] == key:
                row[i], row[-1] = row[-1], row[i]
                row.pop()
                break

    def insert(self, key, value):
        if self.search(key):
            self.remove(key)
        self.table[self.hash_function(key)].append((key, value))


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class HashTable2:  # try separate chaining
    def __init__(self):
        self.size = 97
        self.table = [None] * self.size

    def hash_func(self, key):
        return sum([ord(c) for c in key]) % self.size

    def search(self, key):
        hash_value = self.hash_func(key)
        if not self.table[hash_value]:
            return
        curr = self.table[hash_value]
        while curr:
            if curr.key == key:
                return curr.val
            else:
                curr = curr.next
        return None

    def remove(self, key):
        hash_value = self.hash_func(key)
        if not self.table[hash_value]:
            return
        if self.table[hash_value].key == key:
            self.table[hash_value] = self.table[hash_value].next
        else:
            curr = self.table[hash_value]
            while curr.next:
                if curr.next.key == key:
                    curr.next = curr.next.next
                else:
                    curr = curr.next

    def insert(self, key, value):
        hash_value = self.hash_func(key)
        new_node = Node(key, value)
        if not self.table[hash_value]:
            self.table[hash_value] = new_node
        else:
            curr = self.table[hash_value]
            while curr.next:
                if curr.next.key == key:
                    curr.next.val = value
                    break
                else:
                    curr = curr.next
            curr.next = new_node
        return


def main():
    print('Hash table with separate chaining collision resolution technique')
    hash_table = HashTable()
    hash_table.insert('HAOJIE', 'haha')
    hash_table.insert('ZHUOHUI', 'hoho')
    print(hash_table.search('HAOJIE'))
    print(hash_table.table)

    print('Hash table with separate chaining collision resolution technique')
    ht = HashTable2()
    ht.insert('aaaa', 1111)
    ht.insert('bbbb', 2222)
    print(ht.search('aaaa'))
    print(ht.table)


if __name__ == "__main__":
    main()
