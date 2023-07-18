class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        # print(words)  # ["Let's", 'take', 'LeetCode', 'contest']
        res = []
        for i in range(len(words)):
            res.append(words[i][::-1])
        # print(res)
        return ' '.join(res)


so = Solution()
s = "Let's take LeetCode contest"
test = so.reverseWords(s)
print(test)