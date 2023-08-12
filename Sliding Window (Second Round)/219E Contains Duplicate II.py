from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # sliding window with hashmap
        existed = set()
        left = 0
        for i in range(left, left + k + 1):
            if nums[i] not in existed:
                existed.add(nums[i])
            else:
                return True
        if len(existed) == len(nums):
            return False
        for right in range(left + k + 1, len(nums)):
            existed.remove(nums[left])
            left += 1
            if nums[right] in existed:
                return True
            else:
                existed.add(nums[right])
        return False


s = Solution()
nums = [1,2,3,1,2,3]
k = 2
test = s.containsNearbyDuplicate(nums, k)
print(test)