"""
Runtime: ms647, beat 91%
Difficulty: Median
Solution: binary search, bisect
Time complexity: O(logn)
Space complexity: O(1)
"""
from collections import defaultdict
from bisect import bisect


class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(dict)
        self.stampmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.stampmap[key].append(timestamp)
        self.timemap[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ''
        v = bisect(self.stampmap[key], timestamp)
        if v == 0:
            return ''
        else:
            ans = self.stampmap[key][v - 1]
            return self.timemap[key][ans]


# Your TimeMap object will be instantiated and called as such:
timeMap = TimeMap()
timeMap.set("love","high",10)
timeMap.set("love","low",20)
print(timeMap.timemap)
print(timeMap.stampmap)
print(timeMap.get("love", 5))
print(timeMap.get("love", 10))
print(timeMap.get("love", 15))
print(timeMap.get("love", 20))
print(timeMap.get("love", 25))

print()

timeMap2 = TimeMap()
timeMap2.set("foo", "bar", 1)
print(timeMap2.get("foo", 1))
print(timeMap2.get("foo", 3))
timeMap2.set("foo", "bar2", 4)
print(timeMap2.get("foo", 4))
print(timeMap2.get("foo", 5))