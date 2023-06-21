from typing import List


class SummaryRanges:

    def __init__(self):
        self.ls = []
        self.visited = set()

    def addNum(self, value: int) -> None:
        if value not in self.visited:
            self.ls.append(value)
            self.visited.add(value)

    def getIntervals(self) -> List[List[int]]:
        if len(self.ls) == 0:
            print('len(ls) == 0')
            return []
        self.ls.sort()
        res = []

        def new_ls_merge(new_ls):
            if not new_ls:
                return

            start, prev, size = new_ls[0], new_ls[0], 0
            # print(prev, size)
            for i in new_ls[1:]:
                if i == prev + 1:
                    size += 1
                    prev += 1
                else:
                    res.append([start, start + size])
                    start, prev, size = i, i, 0
            res.append([start, start + size])

        new_ls_merge(self.ls)
        return res


# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
obj.addNum(1)
print(obj.getIntervals())
obj.addNum(3)
print(obj.getIntervals())
obj.addNum(7)
print(obj.getIntervals())
obj.addNum(2)
print(obj.getIntervals())
obj.addNum(6)
print(obj.getIntervals())
obj.addNum(8)
print(obj.getIntervals())
