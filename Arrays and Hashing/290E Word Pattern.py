import collections


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ls = s.split(' ')
        if len(ls) != len(pattern):
            return False
        dic = collections.defaultdict(list)
        for i, e in enumerate(pattern):
            dic[e].append(i)
        print(dic)
        word_set = set()
        for k, index_list in dic.items():
            word = ls[index_list[0]]
            if word in word_set:
                return False
            for index in index_list[1:]:
                if ls[index] != word or ls[index] in word_set:
                    return False
            word_set.add(word)
        return True


so = Solution()
pattern = "aaa"
s = "cat cat cat cat"
test = so.wordPattern(pattern, s)
print(test)