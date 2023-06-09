import collections
from typing import List

"""
这是一道数学题
首先直觉是找到tasks中频率最高的字母，并得出一个简略的思路：A__A__A, n = 2
接下来分为三种情况：
第一种： AAABBB， n = 2. AB_AB_AB, 可知其结果来源于，（频率最高的字母出现的次数-1）*（n+1）+ 频率最高的字母的不同类
第二种： AAABBBC, n = 2, ABCAB_AB, 可轻松证明，当其余字数频率小于A，且其余字数足够填满空位时，结果依然是上面公式
第三种，AAABBBCCDEF， n = 2 ABCDABCEABF，这种情况下，tasks长度超过了空位，逻辑上他们可以首先填满空位，再扩充每个单元即可，结果为len(tasks)
因此结果为：max(len(tasks), (max_freq - 1) * (n + 1) + max_freq_elem_count)
"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        max_freq = max(count.values())
        max_freq_elem_count = 0
        for k, v in count.items():
            if v == max_freq:
                max_freq_elem_count += 1
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_freq_elem_count)


s = Solution()
tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
n = 3
test = s.leastInterval(tasks, n)
print(test)
