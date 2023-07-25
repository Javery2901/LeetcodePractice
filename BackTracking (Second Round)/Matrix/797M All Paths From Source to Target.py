from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []

        def backtracking(index, ls):
            if index == len(graph) - 1:
                res.append(ls[:])
                return
            for i in graph[index]:
                ls.append(i)
                backtracking(i, ls)
                ls.pop()

        backtracking(0, [0])
        return res

s = Solution()
graph = [[4,3,1],[3,2,4],[3],[4],[]]
test = s.allPathsSourceTarget(graph)
print(test)