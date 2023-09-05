from typing import List
"""
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
0 <= j <= nums[i] 
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        end = 0
        farthest = 0

        # Implicit BFS
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                ans += 1
                break
            if i == end:  # Visited all the items on the current level
                ans += 1  # Increment the level
                end = farthest  # Make the queue size for the next level

        return ans


s = Solution()
nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
test = s.jump(nums)
print(test)