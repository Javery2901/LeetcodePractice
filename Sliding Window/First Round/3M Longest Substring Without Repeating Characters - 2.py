class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            print(charSet)
            res = max(res, r - l + 1)
        return res


sol = Solution()
s = "abcabcbb"
res = sol.lengthOfLongestSubstring(s)
print(res)
