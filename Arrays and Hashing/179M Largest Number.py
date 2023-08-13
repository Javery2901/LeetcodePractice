from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(map(bool, nums)):
            return '0'
        str_nums = list(map(str, nums))
        for first in range(len(str_nums) - 1):
            second = first + 1

            while first < len(str_nums) and second < len(str_nums):
                if int(str_nums[first] + str_nums[second]) < int(str_nums[second] + str_nums[first]):
                    # if first string smaller than second string, swap
                    str_nums[first], str_nums[second] = str_nums[second], str_nums[first]
                second += 1
                # 每轮替换，确保first就是最大的
        return ''.join(str_nums)


s = Solution()
nums = [432, 43243]
test = s.largestNumber(nums)
print(test)
