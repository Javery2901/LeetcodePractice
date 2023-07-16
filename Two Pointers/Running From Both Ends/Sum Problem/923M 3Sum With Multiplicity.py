import collections
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        # O(n2)
        arr.sort()
        count = 0
        counter = collections.Counter(arr)  # optimize
        i = 0
        while i < len(arr):
            j = i  # important start from beginning
            k = len(arr) - 1
            while j < k:
                if arr[i] + arr[j] + arr[k] == target:
                    if arr[i] == arr[j] == arr[k]:
                        count += counter[arr[i]] * (counter[arr[i]] - 1) * (counter[arr[i]] - 2) // 6
                    elif arr[i] != arr[j] == arr[k]:
                        count += counter[arr[i]] * (counter[arr[j]]) * (counter[arr[j]] - 1) // 2
                    elif arr[i] == arr[j] != arr[k]:
                        count += counter[arr[i]] * (counter[arr[i]] - 1) * (counter[arr[k]]) // 2
                    else:
                        count += counter[arr[i]] * counter[arr[j]] * counter[arr[k]]
                    j += counter[arr[j]]
                    k -= counter[arr[k]]
                    # print(i, j, k)
                elif arr[i] + arr[j] + arr[k] > target:
                    k -= counter[arr[k]]
                else:
                    j += counter[arr[j]]
            i += counter[arr[i]]
        return count % (10 ** 9 + 7)


s = Solution()
arr = [1,1,2,2,3,3,4,4,5,5]
target = 8
test = s.threeSumMulti(arr, target)
print(test)

