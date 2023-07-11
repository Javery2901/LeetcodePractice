from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)

        def findkth(a, b, target):
            if not a:
                return b[target - 1]
            if not b:
                return a[target - 1]
            median1, median2 = len(a) // 2 + 1, len(b) // 2 + 1
            m1, m2 = a[len(a) // 2], b[len(b) // 2]
            if median1 + median2 > target:
                if m1 > m2:
                    return findkth(a[:median1 - 1], b, target)
                else:
                    return findkth(a, b[:median2 - 1], target)
            else:
                if m1 > m2:
                    return findkth(a, b[median2:], target - median2)
                else:
                    return findkth(a[median1:], b, target - median1)

        if n == 0:
            return (nums2[m // 2 - 1] + nums2[m // 2]) / 2 if m % 2 == 0 else nums2[m // 2]
        if m == 0:
            return (nums1[n // 2 - 1] + nums1[n // 2]) / 2 if n % 2 == 0 else nums1[n // 2]
        if (m + n) % 2 == 0:
            return (findkth(nums1, nums2, (m + n) // 2) + findkth(nums1, nums2, (m + n) // 2 + 1)) / 2
        return findkth(nums1, nums2, (m + n) // 2 + 1)


s = Solution()
nums1 = [0,0]
nums2 = [0,0]
test = s.findMedianSortedArrays(nums1, nums2)
print(test)