from typing import List
"""
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
"""


class Solution:
    def canJump_dp(self, nums: List[int]) -> bool:  # slow
        last_index = len(nums) - 1  # 4
        memo = set()  # if nums[x] cannot reach, put x in the memo and return

        def jump(index):  # start
            memo.add(index)
            if index >= last_index:
                return True
            for i in range(index + nums[index], index, -1):
                if i not in memo:
                    if jump(i):  # 2
                        return True
            return False
        return jump(0)

    def canJump_greedy(self, nums: List[int]) -> bool:  # fast
        reachable_node = 0
        for index, num in enumerate(nums):
            if index + num >= reachable_node:
                reachable_node = index + num
            if index == reachable_node:
                break
        return reachable_node >= len(nums) - 1


s = Solution()
nums = [2,5,0,0]
test = s.canJump_greedy(nums)
print(test)
