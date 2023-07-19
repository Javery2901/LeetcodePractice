class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # idea: group
        group = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                group.append(count)
                count = 1
        group.append(count)

        res = 0
        for i in range(1, len(group)):
            res += min(group[i - 1], group[i])
        return res

    def countBinarySubstrings_two_pointers(self, s: str) -> int:
        left = 0
        right = 1
        res = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                right += 1
            else:
                left, right = right, 1
            if right <= left:
                res += 1
        return res


so = Solution()
s = "00110011"
test = so.countBinarySubstrings_two_pointers(s)
print(test)