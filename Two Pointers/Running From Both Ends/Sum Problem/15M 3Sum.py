from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # O(nlogn)
        ls = []

        for i in range(len(nums)-1):  # O(n2)
            if i > 0 and nums[i-1] == nums[i]:  # important
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ls.append([nums[i], nums[j], nums[k]])
                    j += 1  # important
                    while nums[j-1] == nums[j] and j < k:
                        j += 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return ls


sol = Solution()
nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
res = sol.threeSum(nums)
print(res)