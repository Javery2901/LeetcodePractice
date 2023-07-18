from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two pointers, fast pointer means the original element, slow pointer means the new ordered elements
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
