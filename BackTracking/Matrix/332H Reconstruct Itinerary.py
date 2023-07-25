import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        al = collections.defaultdict(list)
        for departure, arrival in tickets:
            al[departure].append(arrival)
        for value in al.values():
            value.sort()  # 对目的地排序
        # print(al)  # {'JFK': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['JFK', 'SFO']})
        # backtracking is required
        res = []

        def backtracking(ls, from_city):
            if len(ls) == len(tickets) + 1:
                res.append(ls[:])
                return True

            for i, to_city in enumerate(al[from_city]):
                al[from_city].pop(i)
                ls.append(to_city)
                if backtracking(ls, to_city):
                    return True
                ls.pop()
                al[from_city].insert(i, to_city)

        backtracking(['JFK'], 'JFK')
        return res[0]

    def findItinerary_dfs(self, tickets: List[List[str]]) -> List[str]:
        al = collections.defaultdict(list)
        for departure, arrival in tickets:
            al[departure].append(arrival)
        for value in al.values():
            value.sort(reverse=True)  # 对目的地排序
        print(al)  # {'JFK': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['JFK', 'SFO']})
        # backtracking is required
        res = []
        stack = ['JFK']
        while stack:
            elem = stack[-1]
            if elem in al and len(al[elem]) > 0:
                stack.append(al[elem].pop())
            else:
                res.append(stack.pop())
        return res[::-1]


s = Solution()
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
test = s.findItinerary_dfs(tickets)
print(test)