"""
Difficulty: Easy
Solution: Sliding Window
Time complexity: O()
Space complexity: O()
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # left = 0
        # for right in range(len(needle) - 1, len(haystack)):
        #     if haystack[left: right + 1] == needle:
        #         return left
        #     left += 1
        # return -1
    # if needle == " ", it will return o, which is correct.
        m = len(needle)
        n = len(haystack)
        for i in range(0, n - m + 1):
            if haystack[i: i +m] == needle:
                return i
        return -1

sol = Solution()
haystack = "sadbutsad"
needle = "sad"
res = sol.strStr(haystack, needle)
print(res)