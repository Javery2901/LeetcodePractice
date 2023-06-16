from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_list = {}
        for i, s in enumerate(order):
            order_list[s] = i
        # print(order_list)
        for i in range(len(words) - 1):
            next_one = False
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if order_list[words[i][j]] < order_list[words[i + 1][j]]:
                    next_one = True
                    break
                elif order_list[words[i][j]] > order_list[words[i + 1][j]]:
                    return False
            if not next_one and len(words[i]) > len(words[i + 1]):
                return False
            else:
                continue
        return True


s = Solution()
words = ["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"]
order = "zkgwaverfimqxbnctdplsjyohu"
test = s.isAlienSorted(words, order)
print(test)