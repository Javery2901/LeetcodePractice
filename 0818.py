import heapq


def search(nums, n):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= n:
            right = mid
        else:
            left = mid + 1
    return left if nums[left] == n else -1


# nums = [1, 2, 2, 2, 3, 5, 6]
# n = 5
# print(search(nums, n))


class Solution:
    def heapmerge(self, nums):
        hp = []
        res = []
        for i, array in enumerate(nums):
            heapq.heappush(hp, (array[0], i, 0))

        while hp:
            number, nums_index, array_index = heapq.heappop(hp)
            res.append(number)
            array_index += 1
            if array_index < len(nums[nums_index]):
                heapq.heappush(hp, (nums[nums_index][array_index], nums_index, array_index))
        return res


s = Solution()
nums = [[1,3,5], [2,4,6],[0,7]]
print(s.heapmerge(nums))

