class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur['*'] = True

    # {'b': {'a': {'d': {'*': True}}}, 'd': {'a': {'d': {'*': True}}}, 'm': {'a': {'d': {'*': True}}}}
    def search(self, word: str) -> bool:
        def _search_helper(word, index, cur):
            if len(word) == index:
                if '*' in cur:
                    return True
                else:
                    return False
            if word[index] != '.':
                if word[index] not in cur:
                    return False
                return _search_helper(word, index + 1, cur[word[index]])
            else:
                for char in cur:
                    if char != '*' and _search_helper(word, index + 1, cur[char]):
                        return True

        cur = self.root
        if _search_helper(word, 0, cur):
            return True
        return False


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('a')
obj.addWord('a')
# obj.addWord('mad')
param_2 = obj.search('a.')
print(param_2)