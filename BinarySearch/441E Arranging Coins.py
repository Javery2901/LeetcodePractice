class Solution:
    def arrangeCoins_binary_search(self, n: int) -> int:
        left = 0
        right = n // 2 + 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid * (mid + 1) // 2 > n:
                right = mid - 1
            elif mid * (mid + 1) // 2 < n:
                left = mid + 1
            else:
                return mid
        return left - 1


s = Solution()
n = 1
test = s.arrangeCoins_binary_search(n)
print(test)