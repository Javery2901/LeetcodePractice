import math
from typing import List


class Solution:
    def findMaxForm_top_down(self, strs: List[str], m: int, n: int) -> int:
        memo = {}

        def count_zero_one(str):
            m, n = 0, 0
            for i in str:
                if i == '0':
                    m += 1
                else:
                    n += 1
            return m, n

        def sub_max(index, m, n):
            if m < 0 or n < 0:
                return -math.inf
            if index < 0:
                return 0
            if (index, m, n) in memo:
                return memo[(index, m, n)]
            zeros, ones = count_zero_one(strs[index])
            memo[(index, m, n)] = max(sub_max(index - 1, m - zeros, n - ones) + 1, sub_max(index - 1, m, n))
            return memo[(index, m, n)]

        return sub_max(len(strs) - 1, m, n)

    def findMaxForm_bottom_up(self, strs: List[str], m: int, n: int) -> int:
        table = [[0] * (n + 1) for _ in range(m + 1)]
        for str in strs:
            zero, one = str.count('0'), str.count('1')
            for i in range(m, zero - 1, -1):
                for j in range(n, one - 1, -1):
                    table[i][j] = max(1 + table[i - zero][j - one], table[i][j])
        print(table)
        return table[-1][-1]


s = Solution()
strs = ["10","0001","111001","1","0"]
m = 5
n = 3
test = s.findMaxForm_bottom_up(strs, m, n)
print(test)