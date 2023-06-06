class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children
        cur.flag = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children
        return cur.flag

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children
        return True

    def delete(self, word: str) -> None:
        def _delete_helper(node: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                if not node.flag:
                    return False
                node.flag = False
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False

            child = node.children[char]
            should_delete_child = _delete_helper(child, word, index + 1)
            if should_delete_child:
                del node.children[char]
            return len(node.children) == 0 and not node.flag
        _delete_helper(self.root, word, 0)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
