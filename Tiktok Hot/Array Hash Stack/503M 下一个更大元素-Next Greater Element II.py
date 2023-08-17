from cmath import inf
from typing import List
"""
给定一个循环数组 nums （ nums[nums.length - 1] 的下一个元素是 nums[0] ），返回 nums 中每个元素的 下一个更大元素 。

数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1 。
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # O(n2)  this is very slow
        res = [-inf] * len(nums)

        for i in range(len(nums)):
            # from left to right
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    res[i] = nums[j]
                    break
            if res[i] == -inf:
                # means we don't find any element bigger than nums[i] when traversing from left to right
                # now from right to left
                for j in range(i, -1, -1):
                    if nums[i] < nums[j]:
                        res[i] = nums[j]
            if res[i] == -inf:
                res[i] = -1

        return res

    def nextGreaterElements_stack(self, nums: List[int]) -> List[int]:
        stack = []  # [(index, number)]
        max_number = max(nums)  # find the max number first
        res = [-inf] * len(nums)
        for i, n in enumerate(nums):
            while stack and n > stack[-1][1]:
                index, number = stack.pop()
                res[index] = n
            if n == max_number:
                res[i] = -1
                continue
            stack.append((i, n))
        for i, n in enumerate(nums):
            while stack and n > stack[-1][1]:
                index, number = stack.pop()
                res[index] = n

        return res


s = Solution()
nums = [1,2,1]
# nums = [1,2,3,2,1]  # [2,-1,2]
test = s.nextGreaterElements_stack(nums)
print(test)