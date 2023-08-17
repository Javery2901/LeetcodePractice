class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        table = [[0] * x for x in range(1, query_row + 2)]
        table[0][0] = poured
        for i in range(query_row):
            for j in range(len(table[i])):
                remain = table[i][j] - 1
                if remain > 0:
                    table[i + 1][j] += remain / 2
                    table[i + 1][j + 1] += remain / 2
        if table[query_row][query_glass] < 1:
            return table[query_row][query_glass]
        return 1


s = Solution()
poured = 10
query_row = 4
query_glass = 4
test = s.champagneTower(poured, query_row, query_glass)
print(test)