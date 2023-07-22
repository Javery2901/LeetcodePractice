import collections
from typing import List


class Solution:
    def numOfMinutes_dfs(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # use dfs, because we need to go deep to the last one to get the final max_res
        # use a dict to record the index of manager
        dic = collections.defaultdict(list)
        for i, e in enumerate(manager):
            dic[e].append(i)  # {5: [0], 9: [1, 6, 8], 6: [2], 10: [3], -1: [4], 8: [5], 1: [7], 3: [9], 4: [10]}
        # print(dic)

        res = 0
        stack = [(headID, informTime[headID])]
        while stack:
            index, time = stack.pop()
            res = max(res, time)
            for i in dic[index]:
                stack.append((i, time + informTime[i]))
        return res

    def numOfMinutes_bfs(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        dic = collections.defaultdict(list)
        for i, e in enumerate(manager):
            dic[e].append(i)  # {5: [0], 9: [1, 6, 8], 6: [2], 10: [3], -1: [4], 8: [5], 1: [7], 3: [9], 4: [10]}
        # print(dic)
        res = 0
        queue = collections.deque([(headID, informTime[headID])])
        while queue:
            index, time = queue.popleft()
            res = max(res, time)
            for i in dic[index]:
                queue.append((i, time + informTime[i]))
        return res


s = Solution()
n = 11
headID = 4
manager = [5,9,6,10,-1,8,9,1,9,3,4]
informTime = [0,213,0,253,686,170,975,0,261,309,337]
test = s.numOfMinutes_bfs(n, headID, manager, informTime)
print(test)