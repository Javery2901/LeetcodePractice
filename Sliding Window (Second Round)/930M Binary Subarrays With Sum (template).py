"""
Difficulty: Medium
Solution: Sliding Window
Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def less_equal_goal(nums, goal):
            left = 0
            count_one = 0
            count = 0
            for right in range(len(nums)):
                if nums[right] == 1:
                    count_one += 1
                while count_one > goal:
                    if nums[left] == 1:
                        count_one -= 1
                    left += 1
                count += right - left + 1  # 实际记录的是新增的被计数的个数
            print(count)
            return count
        return less_equal_goal(nums, goal) - less_equal_goal(nums, goal - 1)


sol = Solution()
nums = [1,0,1]
goal = 2
res = sol.numSubarraysWithSum(nums, goal)
print(res)