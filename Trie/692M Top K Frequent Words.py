from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_dict = {}
        for word in words:
            words_dict[word] = words_dict.get(word, 0) + 1

        # print(words_dict)
        # reverse k, v in words_dict
        freq_dict = {}
        for key, value in words_dict.items():
            if value not in freq_dict:
                freq_dict[value] = []
            freq_dict[value].append(key)

        # print(freq_dict)
        # {'a': 1, 'aa': 1, 'aaa': 1}
        # {1: ['a', 'aa', 'aaa']}
        final = []
        while k > 0:
            res = []
            max_num = max(freq_dict)
            res.extend(freq_dict[max_num])
            res.sort()
            # print(res)
            k -= len(freq_dict[max_num])
            # print(k)
            if k < 0:
                final.extend(res[: len(res) + k])
                # print(final)
                break
            else:
                final.extend(res)
                del freq_dict[max_num]
        return final


s = Solution()
words = ["a","aa","aaa"]
k = 1
test = s.topKFrequent(words, k)
print(test)
