from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:  # slow
        # important: if you can go from index a to index b
        # then you cant go from any node between a and b to b
        # prove: if a -> a + 1, means gas[a+1] >= gas[a] (gas[a] is 0 at beginning)
        n = len(gas)
        # if sum(cost) > sum(gas):
        #     return -1
        start = 0
        for i in range(n):
            if gas[i] >= cost[i]:
                start = i  # find the start index
                break

        end = start + n
        remaining_gas = 0
        while start < end:
            print(start, remaining_gas, end)
            if gas[start % n] + remaining_gas - cost[start % n] >= 0:
                remaining_gas += gas[start % n] - cost[start % n]
            else:
                end = start + n + 1
                remaining_gas = 0
                if start >= n - 1:
                    break
            start += 1

        if start < end:
            return -1
        return start % n

    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:  # fast
        # important: if you can go from index a to index b
        # then you cant go from any node between a and b to b
        # prove: if a -> a + 1, means gas[a+1] >= gas[a] (gas[a] is 0 at beginning)
        n = len(gas)
        if sum(cost) > sum(gas):
            return -1
        start = 0
        for i in range(n):
            if gas[i] >= cost[i]:
                start = i  # find the start index
                break
        remaining_gas = 0
        index = start
        for i in range(start, n):
            remaining_gas += gas[i] - cost[i]
            if remaining_gas < 0:
                index = i + 1
                remaining_gas = 0
        return index


s = Solution()
gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
test = s.canCompleteCircuit2(gas, cost)
print(test)