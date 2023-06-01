"""
Trapping Water problem: given an array, find the maximum area
Solution: Two pointers

Idea: the left pointer goes from left to right, the right pointer goes from right to left
Update the maximum area every time when the two pointers change

Optimization: when the pointers move, if they are not bigger, we can ignore and continue
Because the area will be sure not bigger than before.
"""


def trapping_water(array) -> int:
    left = 0  # the start index of array
    right = len(array) - 1  # the last index of array
    area = 0
    while left < right:
        min_height = min(array[left], array[right])
        area = max(area, (right - left) * min_height)
        # find a way to update area and height according to different questions
        if array[left] == min_height:
            left += 1
            while array[left] <= min_height and left < right:
                left += 1
                # area -> update according to requirement
        else:
            right -= 1
            while array[right] <= min_height and left < right:
                area -= array[right]
                right -= 1
                # area -> update according to requirement
    return area

