from typing import List

"""
{a:0, b:1,c:-1,d:-1,e:-1}  # 记录最后出现的index

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


