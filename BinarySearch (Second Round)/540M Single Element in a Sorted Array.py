from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # use binary search, check the index

        def check_index(index):  # check if nums[index] appears twice
            # if this is the first one
            if index == 0 or (1 <= index < len(nums) and nums[index - 1] != nums[index]):
                if index % 2 != 0:
                    return True
                else:
                    return False
            else:  # if this is the second one
                if index % 2 != 0:
                    return False
                else:
                    return True

        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if check_index(mid):  # if true, it must be in the left side
                right = mid
            else:
                left = mid + 1
        return nums[left - 1]


s = Solution()
nums = [1,2,2]
test = s.singleNonDuplicate(nums)
print(test)