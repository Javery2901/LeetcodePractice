from typing import List


class Solution:
    def canPartition_memo(self, nums: List[int]) -> bool:
        memo = {}
        if sum(nums) % 2 == 1 or len(nums) == 1 or max(nums) > sum(nums) // 2:
            return False
        target = sum(nums) // 2

        def recursion(index, cur_sum):
            if index == len(nums):
                return False
            if cur_sum == 0:
                return True
            if (index, cur_sum) in memo:
                return memo[(index, cur_sum)]
            memo[(index, cur_sum)] = recursion(index + 1, cur_sum) or recursion(index + 1, cur_sum - nums[index])
            return memo[(index, cur_sum)]

        return recursion(0, target)

    def canPartition_bottom_up(self, nums: List[int]) -> bool:
        # 01背包
        if sum(nums) % 2== 1 or len(nums) == 1 or max(nums) > sum(nums) // 2:
            return False
        target = sum(nums) // 2
        """
             0 1 2 3 4 5 6 target
        0    T F F F F F F
        1(2) T F T F F F F
        2(2) T F T F T F F
        3(5) T F T F T T F
        4(3) T F T T T T F
        index - 1
        """
        table = [[False] * (target + 1) for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            table[i][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if j >= nums[i - 1]:
                    # 当到达index为i的元素时，如果目前的target j与上一个i - 1的元素之差依然在范围内，则可以被取到
                    table[i][j] = table[i - 1][j] or table[i - 1][j - nums[i - 1]]
                else:
                    table[i][j] = table[i - 1][j]
        print(table)
        return table[-1][-1]

    def canPartition_bottom_up2(self, nums: List[int]) -> bool:
        # 01背包
        if sum(nums) % 2== 1 or len(nums) == 1 or max(nums) > sum(nums) // 2:
            return False
        target = sum(nums) // 2
        """
        [T, F, T, T, T, T, F] target
         0  1  2  3  4  5  6
         遍历数组，每次更新一个table。
        """
        table = [False] * (target + 1)
        table[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                # 倒叙，倒序遍历是为了保证物品i只被放入一次！
                # 如果一旦正序遍历，那么物品0就会被重复加入多次
                table[i] = table[i] or table[i - num]
            print(table)
        return table[-1]


s = Solution()
nums= [2,2,5,3]
print(s.canPartition_bottom_up2(nums))

