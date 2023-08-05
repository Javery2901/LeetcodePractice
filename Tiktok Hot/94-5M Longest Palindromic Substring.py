class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 中间扩散
        table = [[1, i] for i in range(len(s))]  # [length, start_index]

        def palindrome(left, right):
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            return right - left - 1, left + 1  # left and right bot move one more round

        left = 0
        while left < len(s):
            right = left + 1
            while right < len(s) and s[left] == s[right]:
                right += 1
            right -= 1
            table[left][0], table[left][1] = palindrome(left, right)
            left += 1

        max_len = 1
        res = s[0]
        for length, start_index in table:
            if length > max_len:
                max_len = length
                res = s[start_index: start_index + length]
        return res


if __name__ == '__main__':
    so = Solution()
    s = "babad"
    print(so.longestPalindrome(s))
