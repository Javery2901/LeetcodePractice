import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)

        while True:
            if k > 1:
                k -= 1
                heapq.heappop(nums)
            else:
                return -heapq.heappop(nums)


s = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
test = s.findKthLargest(nums, k)
print(test)

