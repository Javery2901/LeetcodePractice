from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        # O(n ** 3)
        existed = set()
        res = []
        for a in range(len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):
                c, d = b + 1, len(nums) - 1
                while c < d:
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        if (nums[a], nums[b], nums[c], nums[d]) not in existed:
                            res.append([nums[a], nums[b], nums[c], nums[d]])
                            existed.add((nums[a], nums[b], nums[c], nums[d]))
                        c += 1
                        d -= 1
                        while nums[c - 1] == nums[c] and c < d:
                            c += 1
                        while nums[d + 1] == nums[d] and c < d:
                            d -= 1
                    elif nums[a] + nums[b] + nums[c] + nums[d] > target:
                        d -= 1
                    else:
                        c += 1
        return res


s = Solution()
nums = [2,2,2,2,2]
target = 8
test = s.fourSum(nums, target)
print(test)