"""
Knapsack: Top-down
"""
from math import inf


def knapsack_top_down(V, W, c):
    def aux(c, p):
        if p < 0 or c == 0:
            return 0
        if c < 0:
            return -inf
        if (c, p) not in memo:
            memo[(c, p)] = max(aux(c - W[p], p) + V[p], aux(c, p - 1))
        return memo[(c, p)]

    memo = {}
    return aux(c, len(V) - 1)

# 二维数组，即dp[i][j] 表示从下标为[0-i]的物品里任意取，放进容量为j的背包，价值总和最大是多少。
def knapsack_bottom_up(V, W, c):
    table = [[0] * (c - 1) for _ in range((V) + 1)]

    def get(i, j):
        if 0 < len(table) and 0 <= j < len(table[i]):
            return table[i][j]
        return -inf

    for i in range(1, len(V) + 1):
        for j in range(1, c + 1):
            table[i][j] = max(get(i, j - W[i - 1]), get(i - 1, j))
    return table[-1][-1]

def test_2_wei_bag_problem1(weight, value, bagweight):
    # 二维数组
    dp = [[0] * (bagweight + 1) for _ in range(len(weight))]

    # 初始化
    for j in range(weight[0], bagweight + 1):
        dp[0][j] = value[0]

    # weight数组的大小就是物品个数
    for i in range(1, len(weight)):  # 遍历物品
        for j in range(bagweight + 1):  # 遍历背包容量
            if j < weight[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

    return dp[len(weight) - 1][bagweight]

def test_1_wei_bag_problem(weight, value, bagWeight):
    # 初始化
    # 一维背包，压缩二位背包到一维，并且背包容量需要倒叙进行
    # 原因，由于是一维背包，每次倒叙才能保持前面的值不被随时改变

    dp = [0] * (bagWeight + 1)
    for i in range(len(weight)):  # 遍历物品
        for j in range(bagWeight, weight[i] - 1, -1):  # 遍历背包容量
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    return dp[bagWeight]

if __name__ == "__main__":

    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagweight = 4

    result = test_2_wei_bag_problem1(weight, value, bagweight)
    print(result)