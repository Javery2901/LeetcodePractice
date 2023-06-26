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

