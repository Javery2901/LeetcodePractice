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