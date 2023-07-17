import collections
from typing import List


class Solution:
    def duplicateZeros_stack(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # need to use deque
        queue = collections.deque()
        for i in range(len(arr)):
            queue.append(arr[i])
            if arr[i] == 0:
                queue.append(arr[i])
            arr[i] = queue.popleft()

    def duplicateZeros_math(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        n = len(arr)
        for i in range(n - 1, -1, -1):
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0


s = Solution()
arr = [1,0,2,3,0,4,5,0]
s.duplicateZeros_math(arr)
print(arr)

