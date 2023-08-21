from typing import List

"""
给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
返回一个表示每个字符串片段的长度的列表。

示例 1：
输入：s = "ababcbacadefegdehijhklij"
输出：[9,7,8]
"""

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex = {c: i for i, c in enumerate(s)}
        # print(lastindex)
        # {'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11, 'g': 13, 'h': 19, 'i': 22, 'j': 23, 'k': 20, 'l': 21}
        res = []
        end = 0
        size = 0
        for i, c in enumerate(s):  # need to loop again
            size += 1
            end = max(end, lastindex[c])
            if i == end:
                res.append(size)
                size = 0
        return res



so = Solution()
s = "ababcbacadefegdehijhklij"
test = so.partitionLabels(s)
print(test)


