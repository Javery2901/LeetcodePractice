import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = collections.Counter(t)  # this will not be deleted
        t_counter2 = collections.Counter(t)  # this will be deleted to check first window
        s_counter = collections.Counter(s)
        for i in t_counter:
            if i not in s_counter or t_counter[i] > s_counter[i]:
                return ''
        res = [0, len(s) - 1]
        # sliding window
        left = 0
        for right in range(len(s)):
            # print(left, right)
            if s[right] in t_counter:
                t_counter[s[right]] -= 1
            if s[right] in t_counter2:
                t_counter2[s[right]] -= 1
                if t_counter2[s[right]] == 0:
                    del t_counter2[s[right]]
            if not t_counter2:
                while t_counter[s[left]] < 0 or s[left] not in t_counter:
                    if s[left] in t_counter:
                        t_counter[s[left]] += 1
                    left += 1
                if right - left < res[1] - res[0]:
                    res[0], res[1] = left, right

        # print(res[0], res[1])
        return s[res[0]:res[1] + 1]


so = Solution()
s = "AB"
t = "A"
test = so.minWindow(s, t)
print(test)