from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        table = [0] * (days[-1] + 1)
        days_check = set(days)
        for i in range(1, len(table)):
            if i not in days_check:
                table[i] = table[i - 1]  #
            else:
                table[i] = min(table[max(0, i - 1)] + costs[0],
                               table[max(0, i - 7)] + costs[1],
                               table[max(0, i - 30)] + costs[2])
        print(table)
        return table[-1]


s = Solution()
days = [1,4,6,7,8,20]
costs = [2,7,15]
test = s.mincostTickets(days, costs)
print(test)