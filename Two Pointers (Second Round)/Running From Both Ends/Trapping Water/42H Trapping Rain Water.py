from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # remove 0 from the beginning of list and tail of list
        # two pointer, maintain a variable min_height,
        # the smaller one starts to move, when the next step is smaller, area +=
        # if the next step is bigger, change pointer, maintain the min_height
        i = 0
        j = len(height) - 1
        while height[i] == 0 and i < j:
            i += 1
        while height[j] == 0 and i < j:
            j -= 1
        area = 0
        prev_height = 0
        while i < j:
            min_height = min(height[i], height[j])
            area = area - prev_height + (min_height - prev_height) * (j - i - 1)
            # -prev_height: because this is a column higher than the edge of area, so remove it
            if height[i] == min_height:
                i += 1
                while height[i] <= min_height and i < j:
                    area -= height[i]
                    i += 1
            else:
                j -= 1
                while height[j] <= min_height and i < j:
                    area -= height[j]
                    j -= 1
            prev_height = min_height
        return area


s = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
test = s.trap(height)
print(test)

"""1 11 0
3 11 9
3 10 8
7 10 11
7 7 6
6"""