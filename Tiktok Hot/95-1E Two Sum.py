from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # where the dream starts
        visited = {}  # {number: index}
        for i in range(len(nums)):
            if target - nums[i] in visited:
                return [i, visited[target - nums[i]]]
            visited[nums[i]] = i


