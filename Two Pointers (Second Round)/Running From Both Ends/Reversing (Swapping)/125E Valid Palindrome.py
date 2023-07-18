"""
Runtime: 63ms, beat 31%
Difficulty: Easy
Solution: use two pointers
Time complexity: O(n)
Space complexity: O(1)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer, right_pointer = 0, len(s) - 1
        while left_pointer < right_pointer:
            while left_pointer < right_pointer and not s[left_pointer].isalnum():
                left_pointer += 1
            while left_pointer < right_pointer and not s[right_pointer].isalnum():
                right_pointer -= 1
            if s[left_pointer].lower() != s[right_pointer].lower():
                return False
            else:
                left_pointer += 1
                right_pointer -= 1
        return True


sol = Solution()
s = "0P"
res = sol.isPalindrome(s)
print(res)