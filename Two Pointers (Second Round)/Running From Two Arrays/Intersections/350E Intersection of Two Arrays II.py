import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        existed = collections.defaultdict(int)
        i = j = 0
        nums1.sort()
        nums2.sort()
        while i <len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                existed[nums1[i]] += 1
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        res = []
        for key in existed:
            for _ in range(existed[key]):
                res.append(key)
        return res


s = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
test = s.intersect(nums1, nums2)
print(test)