"""
给你两个版本号 version1 和 version2 ，请你比较它们。

输入：version1 = "1.01", version2 = "1.001"
输出：0
解释：忽略前导零，"01" 和 "001" 都表示相同的整数 "1"

输入：version1 = "1.0", version2 = "1.0.0"
输出：0
解释：version1 没有指定下标为 2 的修订号，即视为 "0"

1 <= version1.length, version2.length <= 500
version1 和 version2 仅包含数字和 '.'
version1 和 version2 都是 有效版本号
version1 和 version2 的所有修订号都可以存储在 32 位整数 中
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        pointer1 = 0
        pointer2 = 0

        while pointer1 < len(version1) or pointer2 < len(version2):
            count1 = count2 = 0
            while pointer1 < len(version1) and version1[pointer1] != '.':
                count1 = count1 * 10 + int(version1[pointer1])
                pointer1 += 1
            while pointer2 < len(version2) and version2[pointer2] != '.':
                count2 = count2 * 10 + int(version2[pointer2])
                pointer2 += 1
            if count1 > count2:
                return 1
            elif count1 < count2:
                return -1
            else:
                pointer1 += 1
                pointer2 += 1
        return 0


s = Solution()
version1 = "1.00001"
version2 = "1.0.001"
test = s.compareVersion(version1, version2)
print(test)
