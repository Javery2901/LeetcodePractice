import collections
from cmath import inf
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False
        target = nums_sum // k
        if max(nums) > target:
            return False

        nums.sort(reverse=True)
        visited = set()

        def backtracking(index, count, curr_sum):
            if count == k:
                return True
            if target == curr_sum:
                return backtracking(0, count + 1, 0)

            for i in range(index, len(nums)):
                if i > 0 and (i - 1) not in visited and nums[i] == nums[i - 1]:
                    continue
                if i in visited or curr_sum + nums[i] > target:
                    continue
                visited.add(i)
                if backtracking(i + 1, count, curr_sum + nums[i]):
                    return True
                visited.remove(i)
            return False

        return backtracking(0, 0, 0)


s = Solution()
# nums = [19,11,1,3,3,1,9,9,3,1]
# k = 3
# nums =[2,2,2,2,3,4,5]
# k = 4
# nums = [4,3,2,3,5,2,1]
# k = 4
nums = [1,1,1,1,2,2,2,2]
k = 2
test = s.canPartitionKSubsets(nums, k)
print(test)