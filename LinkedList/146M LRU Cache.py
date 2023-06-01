from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  # 最新更新的在字典最后
            self.cache[key] = value
            return
        if len(self.cache) == self.capacity:
            self.cache.popitem(False)
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(2, 1)
obj.put(1, 1)
obj.put(2, 3)
obj.put(4, 1)
print(obj.get(1))
print(obj.get(2))

