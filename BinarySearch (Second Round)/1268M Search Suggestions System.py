import bisect
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # binary search
        res = []
        products.sort()
        # print(products)  # ['mobile', 'moneypot', 'monitor', 'mouse', 'mousepad']

        def left_index(start, end, word, index):
            left = start
            right = end
            while left < right:
                mid = left + (right - left) // 2
                if len(products[mid]) > index and  products[mid][index] >= word:
                    right = mid
                else:
                    left = mid + 1
            return left

        def right_index(start, end, word, index):
            left = start
            right = end
            while left < right:
                mid = left + (right - left) // 2
                if len(products[mid]) > index and products[mid][index] > word:
                    right = mid
                else:
                    left = mid + 1
            return left

        start = 0  # the first index
        end = len(products)  # the last in dex

        for i, s in enumerate(searchWord):
            start, end = left_index(start, end, s, i), right_index(start, end, s, i)
            # print(start, end)
            if end - start > 3:
                res.append(products[start: start + 3])
            else:
                res.append(products[start: end])
        return res

    def suggestedProducts_bisect(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()
        prefix = ''
        left = 0
        for s in searchWord:
            prefix += s
            left = bisect.bisect_left(products, prefix, left)
            ls = []
            for prod in products[left: left + 3]:
                if prod.startswith(prefix):
                    ls.append(prod)
            res.append(ls)
        return res


so = Solution()
products = ["havana"]
searchWord = "hjghdg"
test = so.suggestedProducts_bisect(products, searchWord)
print(test)


