from typing import List

'''
Difficulty: Median
Solution: Use a variable to check how many 0 are there in the list
          Three situations: no 0, easy to deal with whole list.
                            one 0, all result except the 0 is 0.
                            two 0, all result is 0.
Time complexity: O(n)
Space complexity: O(1)
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        judge = 0
        for i in nums:
            if i == 0:
                judge += 1
                continue
            pro *= i
        if judge >= 2:
            for i in range(len(nums)):
                nums[i] = 0
        elif judge == 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] = 0
                else:
                    nums[i] = pro
        else:
            for i in range(len(nums)):
                nums[i] = pro // nums[i]
        return nums


s = Solution()
nums = [-1,1,0,-3,0]
res = s.productExceptSelf(nums)
print(res)


