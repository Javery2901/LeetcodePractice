from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers
        # sort the list first, this is to avoid duplicate tuples
        # use set() to check duplicate
        res = []
        existed = set()
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    if (nums[i], nums[left], nums[right]) not in existed:
                        res.append([nums[i], nums[left], nums[right]])
                        existed.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > target:  # means right pointer should go left
                    right -= 1
                else:
                    left += 1
        return res

def main():
    s = Solution()
    nums = [-2,0,0,2,2]
    print(s.threeSum(nums))

if __name__ == '__main__':
    main()