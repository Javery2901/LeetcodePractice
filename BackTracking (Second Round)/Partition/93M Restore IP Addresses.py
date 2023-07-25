from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12 or len(s) < 4:
            return res

        def is_valid(start, end):
            if start > end:
                return False
            if s[start] == '0' and start != end:
                return False
            num = int(s[start: end + 1])
            return 0 <= num <= 255

        def backtracking(index, ls):
            if index == len(s) and len(ls) == 4:
                res.append('.'.join(ls))
                return
            if len(ls) > 4:
                return
            for i in range(index, min(index + 3, len(s))):
                if is_valid(index, i):
                    substring = s[index: i + 1]
                    ls.append(substring)
                    backtracking(i + 1, ls)
                    ls.pop()

        backtracking(0, [])
        return res


so = Solution()
s = "101023"
test = so.restoreIpAddresses(s)
print(test)