from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = list(reversed(digits))  #  [9,9,9,9]
        for i in range(len(res)):
            if res[i] + 1 <= 9:
                res[i] += 1
                break
            else:
                res[i] = 0
            if i == len(res) - 1:
                res.append(1)
                break
        res.reverse()
        return res

    def plusOne_re(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        return self.plusOne_re(digits[:-1]) + [0]


s = Solution()
digits = [9,9,9,9]
test = s.plusOne_re(digits)
print(test)