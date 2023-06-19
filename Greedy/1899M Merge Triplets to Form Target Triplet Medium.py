from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        judge = [0] * n
        exist = [0] * 3  # check if elements == target[i]
        for i, element in enumerate(triplets):
            x, y, z = element[0], element[1], element[2]
            # print(x, y, z)
            if x <= target[0] and y <= target[1] and z <= target[2]:
                judge[i] = 1
                # print(judge)
                if exist[0] == 0 and x == target[0]:
                    exist[0] = 1
                if exist[1] == 0 and y == target[1]:
                    exist[1] = 1
                if exist[2] == 0 and z == target[2]:
                    exist[2] = 1
                # print(exist)

        for i in exist:
            if i == 0:
                return False
        for i in judge:
            if i == 1:
                return True
        return False


s = Solution()
triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]
target = [5,5,5]
test = s.mergeTriplets(triplets, target)
print(test)