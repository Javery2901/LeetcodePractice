from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        res = [-1, -1]
        left, right = 0, len(nums)

        def binary_search(l, r, index, res):
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid
                else:
                    res[index] = mid
                    if index == 0:
                        r = mid
                    else:
                        l = mid + 1

        binary_search(left, right, 0, res)
        if res[0] == -1:
            return [-1, -1]
        else:
            binary_search(left, right, 1, res)
            return res


s = Solution()
nums = [5,7,7,8,8,10]
target = 6
test = s.searchRange(nums, target)
print(test)