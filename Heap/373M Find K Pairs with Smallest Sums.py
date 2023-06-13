from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        queue = [(nums1[0] + nums2[0], 0, 0)]
        res = []
        visited = {(0, 0)}  # record the index of two lists
        while queue and len(res) < k:
            val, idx1, idx2 = heapq.heappop(queue)
            res.append([nums1[idx1], nums2[idx2]])
            if idx1 + 1 < len(nums1) and (idx1 + 1, idx2) not in visited:
                heapq.heappush(queue, (nums1[idx1 + 1] + nums2[idx2], idx1 + 1, idx2))
                visited.add((idx1 + 1, idx2))
            if idx2 + 1 < len(nums2) and (idx1, idx2 + 1 ) not in visited:
                heapq.heappush(queue, (nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1))
                visited.add((idx1, idx2 + 1))
        return res


s = Solution()
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
test = s.kSmallestPairs(nums1, nums2, k)
print(test)