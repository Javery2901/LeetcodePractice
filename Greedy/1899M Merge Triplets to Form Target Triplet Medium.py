from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        exist = [0] * 3  # check if elements == target[i] exist = [False, False, False]

        for i, element in enumerate(triplets):
            x, y, z = element[0], element[1], element[2]
            if x <= target[0] and y <= target[1] and z <= target[2]:
                if exist[0] == 0 and x == target[0]:
                    exist[0] = 1  # exist = [True, False, False]
                if exist[1] == 0 and y == target[1]:
                    exist[1] = 1
                if exist[2] == 0 and z == target[2]:
                    exist[2] = 1

        return exist == [1,1,1]



s = Solution()
triplets = [[2,5,3],[1,8,4],[1,7,5]]
target = [2,7,5]
test = s.mergeTriplets(triplets, target)
print(test)