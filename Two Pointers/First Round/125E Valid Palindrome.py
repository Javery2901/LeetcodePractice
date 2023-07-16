class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = []
        # print(ord('9'))  # A - Z, 65 - 90, a - z, 97 - 122, 0 - 9, 48 - 57
        for i in s:  # O(n)
            if 65 <= ord(i) <= 90:
                i = i.lower()
                ls.append(i)
            elif 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
                ls.append(i)
        left_pointer, right_pointer = 0, len(ls)-1
        judge = True
        while left_pointer <= right_pointer:
            if ls[left_pointer] == ls[right_pointer]:
                left_pointer += 1
                right_pointer -= 1

            else:
                judge = False
                break
        return judge


sol = Solution()
s = "A man, a plan, a canal: Panama"
res = sol.isPalindrome(s)
print(res)