import heapq


class Solution:
    def nthUglyNumber_heapq(self, n: int) -> int:
        if n == 1:
            return 1
        res = []
        heapq.heappush(res, 1)
        existed = {1}
        for _ in range(n - 1):
            num = heapq.heappop(res)
            for factor in (2, 3, 5):
                if num * factor not in existed:
                    heapq.heappush(res, num * factor)
                    existed.add(num * factor)
        return res[0]

    def nthUglyNumber_bottom_up(self, n: int) -> int:
        table = [0] * n
        table[0] = 1
        i, j, k = 0, 0, 0

        for m in range(1, n):
            table[m] = min(table[i] * 2, table[j] * 3, table[k] * 5)
            if table[m] == table[i] * 2:
                i += 1
            if table[m] == table[j] * 3:
                j += 1
            if table[m] == table[k] * 5:
                k += 1
        return table[n - 1]


s = Solution()
n = 11
test = s.nthUglyNumber_bottom_up(n)
print(test)