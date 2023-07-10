class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        left = 0
        right = num // 2 + 1
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid
        return False


s = Solution()
num = 3
test = s.isPerfectSquare(num)
print(test)