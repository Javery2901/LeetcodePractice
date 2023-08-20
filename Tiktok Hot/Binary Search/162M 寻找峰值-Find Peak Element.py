from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # binary search, every time check if it is the peak number, if not,
        # go to the bigger side
        # 题目保证了相邻两个元素一定不相同，所以每次二分只有大于或小于的关系。（要么往更小的地方走，要么往更大的地方走）
        # 无限往大的地方靠近，总能找到某个局部最高点（不一定是全居最高）。
        if len(nums) == 1:
            return nums[0]

        def bigger_direction(number):
            # if left side is bigger, return True, otherwise, return False
            if number == 0:
                return nums[number] > nums[number + 1]
            return nums[number - 1] > nums[number]

        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if bigger_direction(mid):
                right = mid
            else:
                left = mid + 1
        return left - 1 if left > 0 else 0


s = Solution()
nums = [1,122,1,3,5,6,4]
test = s.findPeakElement(nums)
print(test)