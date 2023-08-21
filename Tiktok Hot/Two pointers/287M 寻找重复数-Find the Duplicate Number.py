from typing import List
"""
仅有一个重复的数字，不能修改数组
"""
"""
可看作每个数值指向下一个index的位置。如 1 3 4 2 2
nums[0] = 1 代表位置0保存了一个数1，指向位置1
nums[1] = 3 代表位置1保存了一个数3，指向位置3
nums[3] = 2 代表位置3保存了一个数2，指向位置2
nums[2] = 4 代表位置2保存了一个数4，指向位置4
nums[4] = 2 代表位置4保存了一个数2，指向位置2
位置3 和 位置4 都指向位置2，说明位置2是重复的，返回位置2这个位置即可
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = nums[nums[0]], nums[0]
        while fast != slow:
            print(slow, fast)
            slow = nums[slow]
            fast = nums[nums[fast]]
        print(slow, fast)
        print()
        fast = 0
        while fast != slow:
            print(slow, fast)
            slow = nums[slow]
            fast = nums[fast]
        return fast


s = Solution()
nums = [1,3,4,2,2]
test = s.findDuplicate(nums)
print(test)
