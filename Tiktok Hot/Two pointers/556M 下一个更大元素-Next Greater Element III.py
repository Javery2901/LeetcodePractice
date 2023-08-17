"""
给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。
输入：n = 12
输出：21
"""

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))

        i, j = len(nums) - 1, len(nums) - 1
        # i: find the first index that string[index - 1] < string[index]
        # j: find the first index bigger than string[index - 1]
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i == 0:
            return -1

        while j > i and nums[j] <= nums[i - 1]:
            j -= 1
        # now we find i and j
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        # reverse the right part from index i
        nums[i:] = nums[len(nums) - 1: i - 1: -1]  # ['1', '3', '1', '2']
        res = int(''.join(nums))
        return res if res <= 2 ** 31 - 1 else -1


s = Solution()
n = 1231  # 21
test = s.nextGreaterElement(n)
print(test)
