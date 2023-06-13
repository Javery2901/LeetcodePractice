from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = len(nums) - 1, len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1  # 在这里从末尾开始，找到了一个数大于前一个数的位置，i

        if i == 0:
            # 如果i为0了，则说明整个list都是non-increasing的，
            # 因此没有next pernutaion,直接reverse整个list得到答案
            nums.reverse()
            return

        while nums[j] <= nums[i - 1]:
            # 若i不为0，代表其在list中间某个位置
            # 则其实开始从末尾找到第一个大于i-1的数
            j -= 1
        # 找到后更换位置
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        # 此时j位置上的数已经被处理好了，直接sort数列j后面的数，即i开始的数
        nums[i:] = nums[len(nums) - 1: i - 1: -1]
        return


s = Solution()
nums = [1,3,2]
s.nextPermutation(nums)
print(nums)
