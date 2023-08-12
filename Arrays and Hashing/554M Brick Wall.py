import collections
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        prefix_sum = collections.defaultdict(int)
        for i in range(len(wall)):
            _sum = 0
            for j in range(len(wall[i])):
                if j != len(wall[i]) - 1:
                    _sum += wall[i][j]
                    prefix_sum[_sum] += 1
        # print(prefix_sum)  # {1: 3, 3: 3, 5: 2, 4: 4, 2: 1})
        # key: the location of the gap, value: the number of the gap at corresponding location
        _max = 0
        for k, v in prefix_sum.items():
            _max = max(v, _max)
        return len(wall) - _max


s = Solution()
wall = [[1],[1],[1]]
test = s.leastBricks(wall)
print(test)