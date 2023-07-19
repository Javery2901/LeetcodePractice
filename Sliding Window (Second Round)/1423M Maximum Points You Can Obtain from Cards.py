from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # find a subarray, the sum is minimum
        n = len(cardPoints)
        subarray_sum = current_sum = sum(cardPoints[:n - k])
        print(subarray_sum)
        for i in range(1, k + 1):
            current_sum = current_sum - cardPoints[i - 1] + cardPoints[i + n - k - 1]
            subarray_sum = min(subarray_sum, current_sum)
            print(subarray_sum, current_sum)
        return sum(cardPoints) - subarray_sum


s = Solution()
cardPoints = [1,79,80,1,1,1,200,1]
k = 3
test = s.maxScore(cardPoints, k)
print(test)