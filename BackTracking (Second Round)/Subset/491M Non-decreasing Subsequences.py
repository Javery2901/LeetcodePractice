from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(index, ls):
            if len(ls) > 1:
                res.append(ls[:])

            existed = set()
            for i in range(index, len(nums)):
                if nums[i] in existed:
                    # horizontal, remove the duplicated element
                    continue
                if ls and nums[i] < ls[-1]:
                    # vertical, make sure every new_added element in the ls is the biggest
                    continue
                existed.add(nums[i])
                ls.append(nums[i])
                backtracking(i + 1, ls)
                ls.pop()

        backtracking(0, [])
        return res


s = Solution()
nums = [4,4,6]
print(s.findSubsequences(nums))