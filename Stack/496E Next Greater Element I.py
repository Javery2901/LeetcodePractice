from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # O(n2)
        position = {}
        for i, n in enumerate(nums2):
            position[n] = i
        res = []
        for number in nums1:
            i = position[number] + 1
            while i < len(nums2):
                if nums2[i] > number:
                    res.append(nums2[i])
                    break
                i += 1
            if i == len(nums2):
                res.append(-1)
        return res

    def nextGreaterElement_stack(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        mapping = {}
        for n in nums2:
            while stack and n > stack[-1]:
                mapping[stack.pop()] = n
            stack.append(n)
        while stack:
            mapping[stack.pop()] = -1

        for n in nums1:
            res.append(mapping[n])
        return res


s = Solution()
nums1 = [2,4]
nums2 = [1,2,3,4]  # [-1, 3, -1
test = s.nextGreaterElement_stack(nums1, nums2)
print(test)
