import collections


class Solution:
    def minDistance_bottom_up(self, word1: str, word2: str) -> int:
        # 对每个字母来说，有四种可能，若相等则直接跳过，若不相等则插入或删除或替换，找到最小值
        # if insert, word1 不变， word2 下一位  table[i][j] = table[i][j - 1] + 1
        # if delete, word1 下一位， word2 不变  table[i][j] = table[i - 1][j] + 1
        # if replace, word1 下一位， word2 下一位  table[i][j] = table[i - 1][j - 1] + 1
        if word1 == word2:
            return 0
        if word1 == '' or word2 == '':
            return max(len(word1), len(word2))

        table = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0:
                    table[i][j] = j
                if j == 0:
                    table[i][j] = i
        """
              0('') 1(r)  2(o)  3(s) 
        0('') 0     1     2     3
        0(h)  1     1     2     3
        1(o)  2     2     1     2
        2(r)  3     2     2     2
        3(s)  4     3     3     2
        4(e)  5     4     4     3
        """
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = min(table[i][j - 1], table[i - 1][j], table[i - 1][j - 1]) + 1
                    # [i][j - 1]: insert, [i - 1][j]: delete
        # print(table)
        return table[-1][-1]

    def minDistance_bfs(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        if word1 == '' or word2 == '':
            return max(len(word1), len(word2))
        w1 = list(word1)
        w2 = list(word2)
        count = 0
        queue = collections.deque()
        queue.append((0, 0))
        visited = set()
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                while i < len(w1) and j < len(w2) and w1[i] == w2[j]:
                    i += 1
                    j += 1
                if i == len(w1) and j == len(w2):
                    return count
                queue.append((i, j + 1))
                queue.append((i + 1, j))
                queue.append((i + 1, j + 1))
            count += 1


s = Solution()
word1 = "horse"
word2 = "ros"
test = s.minDistance_bottom_up(word1, word2)
print(test)