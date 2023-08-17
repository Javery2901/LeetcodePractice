from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # need two pointers both go from the back
        # first pointer will find the first index that nums[index] > nums[index - 1]
        # if we didnt find this index (index == 0), reverse the whole nums and return
        # then second pointer will find the first index from right to left that
        # nums[second_pointer] > nums[first_pointer], swap, then reverse the right part of first _pointer
        first = second = len(nums) - 1
        while first >= 1 and nums[first] <= nums[first - 1]:
            first -= 1
        if first == 0:
            nums.reverse()
            return
        while second >= first and nums[second] <= nums[first - 1]:
            second -= 1
        nums[first - 1], nums[second] = nums[second], nums[first - 1]
        nums[first:] = nums[len(nums) - 1: first - 1: -1]


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,6,5,4,3,2,1]
    s.nextPermutation(nums)
    print(nums)


