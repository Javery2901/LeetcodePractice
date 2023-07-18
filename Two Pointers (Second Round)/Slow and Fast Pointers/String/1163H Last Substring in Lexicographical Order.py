class Solution:
    def lastSubstring(self, s: str) -> str:
        fast = 1
        slow = 0
        pointer = 0  # if s[fast] == s[slow], we need to compare the substring one by one
        while fast + pointer < len(s):
            if s[fast + pointer] == s[slow + pointer]:
                pointer += 1
            elif s[fast + pointer] > s[slow + pointer]:
                # we find the bigger one
                slow = max(slow + pointer + 1, fast)
                fast = slow + 1
                pointer = 0  # initialize
            else:  # s[fast + pointer] < s[slow + pointer]:
                fast += pointer + 1
                pointer = 0
        return s[slow:]


so = Solution()
s = "abab"
test = so.lastSubstring(s)
print(test)