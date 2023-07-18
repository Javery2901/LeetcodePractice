"""
Difficulty: Medium
Solution: Sliding Window
Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        trees = set()
        max_tree = 0
        num_trees = 0
        for right in range(len(fruits)):
            if fruits[right] not in trees and len(trees) >= 2:
                left = right
                while fruits[left] == fruits[right]:
                    left -= 1
                while fruits[left] == fruits[left - 1]:
                    left -= 1
                trees = {fruits[left], fruits[right]}
                num_trees = right - left + 1
                max_tree = max(max_tree, num_trees)
            else:
                num_trees += 1
            trees.add(fruits[right])
            max_tree = max(max_tree, num_trees)
        return max_tree


sol = Solution()
fruits = [0,1,6,6,4,4,6]
# fruits = [1,2,1,3,2,2,3,2]
# fruits = [1,2,1]
res = sol.totalFruit(fruits)
print(res)