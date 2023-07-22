"""
# Definition for a QuadTree node.
"""
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:

    def construct(self, grid: List[List[int]]) -> 'Node':

        def zone_check(row_start, col_start, length):
            for i in range(row_start, row_start + length):
                for j in range(col_start, col_start + length):
                    if grid[i][j] != grid[row_start][col_start]:
                        return False
            return True

        def construct_quad(row_start, col_start, length):
            if zone_check(row_start, col_start, length):
                return Node(grid[row_start][col_start], 1)

            node = Node(1, 0)
            node.topLeft = construct_quad(row_start, col_start, length // 2)
            node.topRight = construct_quad(row_start, col_start + length // 2, length // 2)
            node.bottomLeft = construct_quad(row_start + length // 2, col_start, length // 2)
            node.bottomRight = construct_quad(row_start + length // 2, col_start + length // 2, length // 2)
            return node

        return construct_quad(0, 0, len(grid))
