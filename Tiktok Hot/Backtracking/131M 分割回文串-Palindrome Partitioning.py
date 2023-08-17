from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sublist = []

        def palindrome(substr):
            if len(substr) == 1:
                return True
            left, right = 0, len(substr) - 1
            while left < right:
                if substr[left] != substr[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs_backtracking(index):

            if index == len(s):
                res.append(list(sublist))
                return

            for i in range(index, len(s)):
                substring = s[index: i + 1]  # important
                if palindrome(substring):
                    sublist.append(substring)
                    dfs_backtracking(i + 1)
                    sublist.pop()

        dfs_backtracking(0)
        return res


so = Solution()
s = "aab"
test = so.partition(s)
print(test)
