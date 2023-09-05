"""
用两个heapq，每轮分别加入数字, 如[1,2,3,4,5], min_heap储存所有较小数中最大的，max_heap 储存所有最大数中最小的
round 1: min_heap = [-1]
round 2: 2 > -min_heap[0], 故加入max_heap
round 3: 3 > -min_heap[0], 故加入max_heap
round 4：4 > -min_heap[0], 故加入max_heap, 与此同时，pop出max_heap,加入min_heap

"""
import heapq


class MedianFinder:

    def __init__(self):
        self.max_hq = []
        self.min_hq = []

    def addNum(self, num: int) -> None:
        if not self.min_hq or num <= -self.min_hq[0]:
            heapq.heappush(self.min_hq, -num)
        else:
            heapq.heappush(self.max_hq, num)
        if abs(len(self.min_hq) - len(self.max_hq)) > 1:
            if len(self.min_hq) > len(self.max_hq):
                heapq.heappush(self.max_hq, -heapq.heappop(self.min_hq))
            else:
                heapq.heappush(self.min_hq, -heapq.heappop(self.max_hq))
        print('min_hq =', self.min_hq)
        print('max_hq =', self.max_hq)

    def findMedian(self) -> float:
        if len(self.min_hq) == len(self.max_hq):
            return round((-self.min_hq[0] + self.max_hq[0]) / 2, 5)
        else:
            if len(self.min_hq) > len(self.max_hq):
                return round(-self.min_hq[0], 5)
            else:
                return round(self.max_hq[0], 5)


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
print(obj.findMedian())
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
obj.addNum(4)
print(obj.findMedian())
obj.addNum(5)
print(obj.findMedian())
