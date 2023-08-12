from typing import List


class Solution:
    def containsNearbyDuplicate_array(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        existed = {}
        for right in range(len(nums)):
            if nums[right] in existed:
                if right - existed[nums[right]] <= k:
                    return True
            existed[nums[right]] = right
        # print(existed)
        return False
