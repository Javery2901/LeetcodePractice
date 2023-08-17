from typing import List


class Solution:
    def trap_two_pointers(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        while height[left] == 0 and left < right:
            left += 1
        while height[right] == 0 and left < right:
            right -= 1
        area = 0
        prev_height = 0
        while left < right:
            min_height = min(height[left], height[right])
            area += (min_height - prev_height) * (right - left - 1) - prev_height
            if min_height == height[left]:
                left += 1
                while left < right and height[left] <= min_height:
                    area -= height[left]
                    left += 1
            else:
                right -= 1
                while left < right and height[right] <= min_height:
                    area -= height[right]
                    right -= 1
            prev_height = min_height
        return area

    def trap_dp(self, height: List[int]) -> int:
        left_table = [height[0]] * len(height)
        right_table = [height[-1]] * len(height)
        for i in range(1, len(height)):
            if height[i] > left_table[i - 1]:
                left_table[i] = height[i]
            else:
                left_table[i] = left_table[i - 1]
        for i in range(len(height) - 2, - 1, - 1):
            if height[i] > right_table[i + 1]:
                right_table[i] = height[i]
            else:
                right_table[i] = right_table[i + 1]
        total_area = 0
        for i in range(len(height)):
            total_area += min(left_table[i], right_table[i]) - height[i]
        return total_area


if __name__ == '__main__':
    s = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(s.trap_dp(height))