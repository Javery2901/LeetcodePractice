"""
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace" ，它的长度为 3 。
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        table = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text2[i - 1] == text1[j - 1]:
                    table[i][j] += 1 + table[i - 1][j - 1]
                else:
                    table[i][j] += max(table[i - 1][j], table[i][j - 1])
        print(table)
        return table[-1][-1]


s = Solution()
text1 = "bcbbb"
text2 = "bbbcb"
test = s.longestCommonSubsequence(text1, text2)
print(test)