import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = collections.defaultdict(int)
        left = 0
        res = 0
        max_element = 0
        for right in range(len(s)):
            dic[s[right]] += 1
            max_element = max(max_element, dic[s[right]])
            print(max_element)
            if right - left + 1 - max_element > k:  # 固定窗口操作
                dic[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            print(left, right)
        return res


so = Solution()
s = "BAAABCDE"
k = 2
test = so.characterReplacement(s, k)
print(test)
