from typing import List


class Solution:
    def twoSum_two_pointer(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

    def twoSum_binary_search(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):  # not optimal
            start = i
            end = len(numbers) - 1
            while start <= end:
                j = (start + end) // 2
                # print(i, j)
                if target - numbers[i] == numbers[j]:
                    if i == j:
                        end += 1
                    else:
                        return [i + 1, j + 1]
                elif target - numbers[i] < numbers[j]:
                    end = j - 1
                else:
                    start = j + 1


sol = Solution()
numbers = [2, 7, 11, 15]
target = 9
res = sol.twoSum_two_pointer(numbers, target)
print(res)
