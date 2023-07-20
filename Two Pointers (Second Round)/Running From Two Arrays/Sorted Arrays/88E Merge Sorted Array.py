from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # from back to front
        # reorganize the num1 from last index
        # two pointers, one pointing to nums1[m - 1], one pointing to nums2[n - 1]
        pointer1 = m - 1
        pointer2 = n - 1
        i = len(nums1) - 1
        while pointer2 >= 0:
            if nums1[pointer1] <= nums2[pointer2]:
                nums1[i] = nums2[pointer2]
                pointer2 -= 1
            else:
                nums1[i] = nums1[pointer1]
                pointer1 -= 1
            i -= 1

