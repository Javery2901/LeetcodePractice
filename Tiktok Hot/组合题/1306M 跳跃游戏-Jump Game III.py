from typing import List
"""
有一个非负整数数组arr，位于下标i处时，可以跳到i + arr[i]或者i - arr[i].
请判断是否能否跳到对应元素值位0的任一下标处。
"""

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if start < 0 or start >= len(arr) or arr[start] == -1:
            return False

        if arr[start] == 0:
            return True

        jump = arr[start]
        arr[start] = -1  # Mark the current index as visited

        return self.canReach(arr, start + jump) or self.canReach(arr, start - jump)