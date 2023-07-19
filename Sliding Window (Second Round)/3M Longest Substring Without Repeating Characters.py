class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        existed = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in existed:
                existed.remove(s[left])
                left += 1
            existed.add(s[right])
            print(left, right)
            print(existed)
            res = max(res, right - left + 1)
        return res


so = Solution()
s = "pwwkew"
test = so.lengthOfLongestSubstring(s)
print(test)