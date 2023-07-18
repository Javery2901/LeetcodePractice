"""
Difficulty: Medium
Solution: Sliding Window
Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_len = float('-inf')
        adict = defaultdict(int)
        for right in range(len(fruits)):
            adict[fruits[right]] += 1
            while len(adict) > 2:
                adict[fruits[left]] -= 1
                if adict[fruits[left]] == 0:
                    del adict[fruits[left]]
                left += 1
            max_len = max(max_len, right - left + 1)
        if max_len == float('-inf'):
            return 0
        else:
            return max_len


sol = Solution()
fruits = [0,1,6,6,4,4,6]
# fruits = [1,2,1,3,2,2,3,2]
# fruits = [1,2,1]
res = sol.totalFruit(fruits)
print(res)