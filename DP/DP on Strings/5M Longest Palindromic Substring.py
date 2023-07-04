class Solution:
    def longestPalindrome_two_pointers(self, s: str) -> str:
        if len(s) == 1:
            return s
        table = [[1, i] for i in range(len(s))]  # [length, start_index]

        def palindrome(left, right):
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            return right - left - 1, left + 1,

        left = 0
        while left < len(s):
            right = left + 1
            while right < len(s) and s[left] == s[right]:
                right += 1
            right -= 1
            table[left][0], table[left][1] = palindrome(left, right)
            left += 1

        # print(table)
        max_len = 1
        output = s[0]
        for length, start_index in table:
            if length > max_len:
                max_len = length
                output = s[start_index: start_index + length]
        return output

    def longestPalindrome_bottom_up(self, s: str) -> str:
        table = [[False] * len(s) for _ in range(len(s))]
        longest_palindrome_index = (0, 1)  # start from 0, end at 1
        for i in range(len(s)):
            table[i][i] = True
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    if j - i == 1 or table[i + 1][j - 1]:
                        table[i][j] = True
                        if longest_palindrome_index[1] - longest_palindrome_index[0] < j - i + 1:
                            longest_palindrome_index = (i, j + 1)
        left, right = longest_palindrome_index[0], longest_palindrome_index[1]
        return s[left: right]


so = Solution()
s = 'ac'
test = so.longestPalindrome_bottom_up(s)
print(test)