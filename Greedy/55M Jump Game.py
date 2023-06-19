from typing import List


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
