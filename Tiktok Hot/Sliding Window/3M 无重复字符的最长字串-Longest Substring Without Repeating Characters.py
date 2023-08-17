class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        left = 0
        existed = set()
        res = 0
        for right in range(len(s)):
            if s[right] not in existed:
                res = max(right - left + 1, res)
            else:
                while s[right] in existed:
                    existed.remove(s[left])
                    left += 1
            existed.add(s[right])
        return res


so = Solution()
s = "pwwkew"
print(so.lengthOfLongestSubstring(s))


