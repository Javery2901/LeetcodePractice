import heapq
from random import randint
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []
        for n in nums:
            heapq.heappush(hq, -n)
        while k > 1:
            heapq.heappop(hq)
            k -= 1
        return -hq[0]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        hq = []
        for n in nums:
            if len(hq) < k:
                heapq.heappush(hq, n)
            else:
                if n > hq[0]:
                    heapq.heappop(nums)
                    heapq.heappush(hq, n)
        return hq[0]


class Solution2:
    def partition(self, nums: List[int], left: int, right: int) -> int:  # quick select
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1

        nums[fill], nums[right] = nums[right], nums[fill]

        return fill

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1

        while left < right:
            pivot = self.partition(nums, left, right)

            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break

        return nums[k]

    def findKthLargest4(self, nums, k):
        # Solution3. Quick Slection with Random Pivot
        # Time Complexity O(n)
        def partition(nums, left, right):
            ranPivotIndex = randint(left, right)
            pivot = nums[ranPivotIndex]
            pointer = left
            nums[left], nums[ranPivotIndex] = nums[ranPivotIndex], nums[left]

            for i in range(left + 1, right + 1):
                if nums[i] < pivot:
                    pointer += 1
                    nums[i], nums[pointer] = nums[pointer], nums[i]
            nums[left], nums[pointer] = nums[pointer], nums[left]
            return pointer

        left, right = 0, len(nums) - 1
        k = len(nums) - k
        # nums is sorted in the ascending order,
        # So finding the kth largest is trying to get the index of len(nums) - k
        while left < right:
            index = partition(nums, left, right)
            # The value for the location of 'index' has been found
            if index >= k:
                right = index
            else:
                left = index + 1
        return nums[left]


if __name__ == '__main__':
    s = Solution2()
    nums = [3,2,1,5,6,4,7]
    k = 3
    print(s.findKthLargest(nums, k))






