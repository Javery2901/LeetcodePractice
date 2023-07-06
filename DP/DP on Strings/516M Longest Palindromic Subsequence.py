class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # reverse s, actually this is to find the longest common subsequence
        # leetcode 1143
        s2 = s[::-1]
        table = [[0] * (len(s) + 1) for _ in range(len(s2) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(s2) + 1):
                if s[i - 1] == s2[j - 1]:
                    table[i][j] = 1 + table[i - 1][j - 1]
                else:
                    table[i][j] = max(table[i - 1][j], table[i][j - 1])
        return table[-1][-1]


so = Solution()
s = "bbbab"
test = so.longestPalindromeSubseq(s)
print(test)
