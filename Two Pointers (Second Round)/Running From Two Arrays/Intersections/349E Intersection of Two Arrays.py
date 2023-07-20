from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        existed = set()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                existed.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return list(existed)


s = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
test = s.intersection(nums1, nums2)
print(test)