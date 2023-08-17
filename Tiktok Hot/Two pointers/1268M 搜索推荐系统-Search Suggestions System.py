from typing import List
"""
给你一个产品数组 products 和一个字符串 searchWord ，products  数组中每个产品都是一个字符串。
输入：products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
输出：[["mobile","moneypot","monitor"],
      ["mobile","moneypot","monitor"],
      ["mouse","mousepad"],
      ["mouse","mousepad"],
      ["mouse","mousepad"]]
      
1 <= products.length <= 1000
1 <= Σ products[i].length <= 2 * 10^4
products[i] 中所有的字符都是小写英文字母。
1 <= searchWord.length <= 1000
searchWord 中所有字符都是小写英文字母。
"""


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()
        # print(products)  # ['coddle', 'coddles', 'code', 'codephone', 'codes']
        left, right = 0, len(products) - 1
        for i in range(len(searchWord)):
            ch = searchWord[i]
            while left <= right and (len(products[left]) <= i or products[left][i] != ch):
                left += 1
            while left <= right and products[right][i] != ch:
                right -= 1
            valid_range = right - left + 1
            words = []
            for j in range(min(3, valid_range)):
                words.append(products[left + j])
            res.append(words)
        return res


s = Solution()
products = ['coddle', 'coddles', 'code', 'codephone', 'codes']
searchWord = "codes"
test = s.suggestedProducts(products,searchWord)
print(s.suggestedProducts(products, searchWord))