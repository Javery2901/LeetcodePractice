from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        table = [[1] * i for i in range(1, numRows + 1)]
        for i in range(len(table)):
            for j in range(len(table[i])):
                if j == 0 or j == len(table[i]) - 1:
                    continue
                # when i == 2, j == 1
                table[i][j] = table[i - 1][j - 1] + table[i - 1][j]
        return table

s = Solution()
numRows = 5
test = s.generate(numRows)
print(test)