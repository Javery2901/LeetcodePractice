from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        def check(index):
            remove_index = set(removable[:index + 1])  # {3} O(n)
            s_pointer, p_pointer = 0, 0
            while s_pointer < len(s) and p_pointer < len(p):
                if s_pointer not in remove_index:
                    if s[s_pointer] == p[p_pointer]:
                        p_pointer += 1
                s_pointer += 1
            return p_pointer == len(p)  # if True, means subsequence

        left = 0
        right = len(removable)
        while left < right:
            mid = left + (right - left) // 2
            if not check(mid):
                right = mid
            else:
                left = mid + 1

        return left


so = Solution()
s = "abcab"
p = "abc"
removable = [0,1,2,3,4]
test = so.maximumRemovals(s, p, removable)
print(test)