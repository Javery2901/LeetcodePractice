class Solution:
    def validPalindrome(self, s: str) -> bool:

        def palindrome(l, r, judge):
            if l == r:
                return True
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    if judge == 1:
                        return False
                    return palindrome(l + 1, r, 1) or palindrome(l, r - 1, 1)
            return True

        left, right = 0, len(s) - 1
        return palindrome(left, right, 0)


so = Solution()
s = "abc"
test = so.validPalindrome(s)
print(test)