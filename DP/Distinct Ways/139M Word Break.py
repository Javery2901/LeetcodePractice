from typing import List


class Solution:
    def wordBreak_backtracking(self, s: str, wordDict: List[str]) -> bool:
        # TLE on the case
        # "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        # ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        word_Set = set(wordDict)

        def backtracking(index):
            print(index)
            if index == len(s):
                return True

            word = ''
            for i in range(index, len(s)):
                word += s[i]
                if word in word_Set:
                    if backtracking(i + 1):
                        return True
            return False

        return backtracking(0)

    def wordBreak_top_down(self, s: str, wordDict: List[str]) -> bool:
        # 广义上看top_down 是添加了memo的backtracking
        memo = {}
        word_Set = set(wordDict)

        def recursion(start):
            if start >= len(s):
                return True
            if start in memo:
                return memo[start]
            for i in range(start + 1, len(s) + 1):
                word = s[start: i]
                if word in word_Set:
                    if recursion(i):
                        return True
            memo[start] = False
            return memo[start]

        recursion(0)
        # print(memo)
        return memo[0]

    def wordBreak_bottom_up(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        table = [False] * (1 + len(s))
        table[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if table[j] and s[j: i] in word_set:
                    table[i] = True
        print(table)
        return table[-1]


so = Solution()
s = "leetcode"
wordDict = ["leet","code"]
# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]
# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
test = so.wordBreak_bottom_up(s, wordDict)
print(test)
