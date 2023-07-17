from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find the index of x first
        if x <= arr[0]:
            return arr[:k]
        if x >= arr[-1]:
            return arr[-k:]

        left = 0
        right = len(arr) - 1
        # two pointers
        while right - left + 1 > k:  # important
            if abs(x - arr[left]) > abs(x - arr[right]):
                left += 1
            else:
                right -= 1
        return arr[left: right + 1]


s = Solution()
arr = [0, 1, 1, 1, 2, 3, 6, 7, 8, 9]
k = 9
x = 4
test = s.findClosestElements(arr, k, x)
print(test)
