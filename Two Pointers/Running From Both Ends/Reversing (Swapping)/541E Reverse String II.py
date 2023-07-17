class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ls = list(s)

        times = len(ls) // (2 * k)
        left = len(ls) % (2 * k)
        for i in range(1, times + 1):
            ls[(i - 1) * 2 * k: (i - 1) * 2 * k + k] = reversed(ls[(i - 1) * 2 * k: (i - 1) * 2 * k + k])
        if left < k:
            ls[times * (2 * k):] = reversed(ls[times * (2 * k):])
        else:  # k <= left < 2k
            ls[times * (2 * k): times * (2 * k) + k] = reversed(ls[times * (2 * k): times * (2 * k) + k])
        return ''.join(ls)


so = Solution()
s = "abcdefg"
k = 2
test = so.reverseStr(s, k)
print(test)