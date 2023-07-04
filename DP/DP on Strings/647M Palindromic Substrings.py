class Solution:
    def countSubstrings_bottom_up(self, s: str) -> int:
        count = len(s)
        table = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            table[i][i] = True

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    if j - i == 1 or table[i + 1][j - 1]:
                        table[i][j] = True
                        count += 1
        return count


so = Solution()
s = "aab"
test = so.countSubstrings_bottom_up(s)
print(test)