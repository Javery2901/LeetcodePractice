from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        fast, slow = 1, 1
        count = 1
        for fast in range(1, len(chars)):
            if chars[fast] == chars[fast - 1]:
                count += 1
            else:
                if count != 1:
                    for i in str(count):
                        chars[slow] = i
                        slow += 1
                chars[slow] = chars[fast]
                slow += 1
                count = 1

        if slow == len(chars):
            return slow

        if count == 1:
            chars[slow] = chars[fast]

        else:
            for i in str(count):
                chars[slow] = i
                slow += 1
        return slow


s = Solution()
chars = ["a","a","a","a","a","b"]
test = s.compress(chars)
print(test)
