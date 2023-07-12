from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()  # [1,2,3,4,5]
        res = [0] * len(spells)
        for i, spell in enumerate(spells):
            left = 0
            right = len(potions)
            while left < right:
                mid = left + (right - left) // 2
                if potions[mid] * spell >= success:
                    right = mid
                else:
                    left = mid + 1
            res[i] = len(potions) - left
        return res


s = Solution()
spells = [3,1,2]
potions = [8,5,8]
success = 16
test = s.successfulPairs(spells, potions, success)
print(test)