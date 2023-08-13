import collections


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # 记录每个出现的字母的最开始和最末尾值
        # 这之间的用set去重，set长度即为这个字母开始和结尾的个数
        s_dict = collections.defaultdict()
        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = [i, i]
            else:
                s_dict[s[i]][1] = i
        # print(s_dict)  # {'a': [0, 4], 'b': [2, 2], 'c': [3, 3]})
        res = 0
        for char, char_range in s_dict.items():
            if char_range[1] - char_range[0] <= 1:
                continue
            res += len(set(s[char_range[0] + 1: char_range[1]]))
            # print(res)
        return res


so = Solution()
s = "abcdefgabcdefg"
test = so.countPalindromicSubsequence(s)
print(test)