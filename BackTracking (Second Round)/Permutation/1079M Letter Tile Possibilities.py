import collections


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = [0]
        counter = collections.Counter(tiles)
        tiles_set = set(list(tiles))

        def backtracking(ls, tiles_set):
            if ls:
                res[0] += 1

            # for i in counter:  # important
            for i in tiles_set:  # important: remove duplicate
                if counter[i]:
                    counter[i] -= 1
                    ls.append(i)
                    backtracking(ls, tiles_set)
                    ls.pop()
                    counter[i] += 1

        backtracking([], tiles_set)
        return res[0]


s = Solution()
tiles = "AAB"
test = s.numTilePossibilities(tiles)
print(test)