"""
Difficulty: Medium
Solution: Sliding Window
Time complexity: O()
Space complexity: O()
"""
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len(s1)])
        if s1_counter == s2_counter:
            return True
        print(s2_counter)
        for i in range(len(s1), len(s2)):
            if s1_counter == s2_counter:  # check if they are the same
                return True
            s2_counter[s2[i-len(s1)]] -= 1  # window sliding, left moving
            s2_counter[s2[i]] += 1  # window sliding, right moving
            print(s2_counter)
        return s1_counter == s2_counter


sol = Solution()
s1 = "ab"
s2 = "eidbaooo"
res = sol.checkInclusion(s1, s2)
print(res)
