"""
Kadane's algorithm（卡登算法）是一种用于解决最大子数组和问题的动态规划算法。
最大子数组和问题是指在一个数组中找到一个具有最大和的连续子数组。
通过在每一步迭代中，维护两个变量来实现。第一个变量是当前子数组的最大和，称为current_max，
第二个变量是全局最大和，称为global_max。
time complexity: O(n), space complexity: O(1)

算法的步骤如下：
1. 初始化current_max和global_max为数组的第一个元素。
2. 对于数组中的每个元素（从第二个元素开始），执行以下操作：
    2.1 将当前元素添加到当前子数组的末尾，更新current_max为当前子数组的最大和（包括当前元素）和当前元素本身中的较大值。
    2.2 更新global_max为current_max和global_max中的较大值，以便保留最大的子数组和。
3. 最终，global_max将包含整个数组中的最大子数组和。

理解：
1. 对一个数组A[0...n]从左向右扫描，假设到达第j个数值，它会计算结束于A[j]的子数组中的最大和，并将其保存在current_max中
2. 与此同时，它会保存从A[0]到A[j]子数组中的任意一串位置的最大和，并将其保存于best_sum中。直至结束
"""
from typing import List


def max_subarray(numbers: List[int]) -> int:
    """Find the largest sum of any contiguous subarray."""
    if not numbers:
        return 0
    best_sum = numbers[0]
    current_sum = numbers[0]
    for x in numbers[1:]:
        current_sum = max(x, current_sum + x)
        # 当current_sum 每次选择x时，代表subarray从x重新开始了
        best_sum = max(best_sum, current_sum)
        # 每当best_sum更新一次的时候，代表subarray变更了
        # 当best_sum不更新时，代表最优的subarray还是之前的样子
    return best_sum