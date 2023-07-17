class Solution:

    def reverseWords_optimal(self, s: str) -> str:
        words = s.split(' ')
        # print(words)  # ['a', 'good', '', '', 'example']
        res = []
        while words:
            word = words.pop()
            if word.strip() == '':
                continue
            res.append(word)
        return ' '.join(res)


    def reverseWords(self, s: str) -> str:
        # count how many words is in the s
        i = 0
        count = 0

        while i < len(s):
            if s[i] == ' ':
                i += 1
            else:
                count += 1
                while i < len(s) and s[i] != ' ':
                    i += 1
        res = [''] * count

        left, right = 0, len(s) - 1
        l_word = 0
        r_word = count - 1
        while left <= right:
            while left <= right and s[left] == ' ':
                left += 1
            while left <= right and s[right] == ' ':
                right -= 1
            left_word = []
            right_world = []
            while left <= right and s[left] != ' ':
                left_word.append(s[left])
                left += 1
            while left <= right and s[right] != ' ':
                right_world.append(s[right])
                right -= 1
            right_world.reverse()
            # print(left_word, right_world)
            if left_word:
                res[r_word] = ''.join(left_word)
                r_word -= 1
            if right_world:
                res[l_word] = ''.join(right_world)
                l_word += 1
        # print(res)  # ['example', 'good', 'a']
        return ' '.join(res)


so = Solution()
s = "a good   example"
test = so.reverseWords_optimal(s)
print(test)