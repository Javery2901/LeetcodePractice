class Solution:
    def jane_street_bottom_up(self, nums: list, target: int) -> int:
        """
             0  1  2  3  4  target
        0(1) 0  1  0  0  0
        1(1) 0  3  0  0  0
        2(2) 0  3  4  0  0
        3(0) 8  3  4  0  0
        4(3) 16 3  4  4  0
        5(4) 32 3  4  4  0
        index
        """
        table = [[0] * (target + 1) for _ in range(len(nums))]
        for i in range(len(nums)):  # target
            for j in range(target + 1):  # index start from 0
                if nums[i] == j:
                    table[i][j] += 1
                if i > 0:
                    table[i][j] += table[i - 1][j]  # the cases without nums[i]
                    # the cases with nums[i]
                    # two situations: 0 in the nums and target is 0
                    if nums[i] == 0:
                        if j == 0:
                            table[i][j] += 2 ** i - 1
                    else:
                        if j % nums[i] == 0:
                            table[i][j] += table[i - 1][j // nums[i]]
        # print(table)
        return table[len(nums) - 1][target]


s = Solution()
nums = [1,1,2,0,3,4]
target = 4
test = s.jane_street_bottom_up(nums, target)
print(test)