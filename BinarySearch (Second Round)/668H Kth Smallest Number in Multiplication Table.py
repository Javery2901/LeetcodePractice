class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        def count(index):
            num = 0
            for i in range(1, m + 1):  # count row by row
                add = min(index // i, n)  # this is important, we can count row by row
                if add == 0:
                    break
                num += add
            return num >= k

        left = 0
        right = m * n
        while left < right:
            mid = left + (right - left) // 2
            if count(mid):  # means mid is smaller than k
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()
m = 2
n = 3
k = 3
test = s.findKthNumber(m, n, k)
print(test)