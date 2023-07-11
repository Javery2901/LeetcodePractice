from collections import defaultdict
from bisect import bisect


class TimeMap:

    def __init__(self):
        self.key_value = {}  # {'foo': ['bar', 'bar2']}
        self.key_time = {}  # {'foo':[1, 4]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_value:
            self.key_value[key] = [value]
            self.key_time[key] = [timestamp]
        else:
            self.key_value[key].append(value)
            self.key_time[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_value:
            return ''
        if timestamp < self.key_time[key][0]:
            return ''
        # now we know key must in key_value and in key_time
        # use binary search to find the correct index
        left = 0  # 0
        right = len(self.key_time[key])  # 1
        while left < right:
            mid = left + (right - left) // 2
            if self.key_time[key][mid] == timestamp:
                return self.key_value[key][mid]
            elif self.key_time[key][mid] > timestamp:
                right = mid
            else:
                left = mid + 1
        return self.key_value[key][left - 1]


class TimeMap2:

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
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)