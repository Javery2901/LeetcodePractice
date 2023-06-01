"""
滑动窗口问题可分为两类，定长滑动窗口和不定长滑动窗口
定长滑动窗口：以 leetcode 28 和 leetcode 567为典型
定长滑动窗口思路较为简单，在for loop中根据窗口长度，从左往右滑动即可。
不定长滑动窗口：以 leetcode 3 和 leetcode 209 为典型
不定长滑动窗口需仔细考虑窗口缩小或者扩大的变化情况。在for loop循环中，常常需要分两部分考虑。
其中一部分更新窗口左边left值以及其带来的影响。这部分可能通过if或while两种方式实现。
如何判断右指针回缩：题目常常存在恰好等于的目标值。（滑动窗口问题就两类：一类是要求值小于等于goal，另一类是恰好等于goal）。以 leetcode 992 和 leedcode 930 为典型。
方法：引入前缀和的方法。将和等于goal改变成和小于等于goal的问题：less_equal(goal) - less_equal(goal - 1)
"""
from typing import List


class Solution:
    def fixed_sliding_window(self, s1: str, s2: str) -> bool:
        left = 0
        for right in range(len(s1) - 1, len(s2)):
            # fixed window, the width of window is often the length of some input
            # check if the substring in window is related to s1
            # change the condition according to different requirement
            if s2[left: right + 1] == template:
                return True
            else:
                left += 1
        return False

    def unfixed_sliding_window(self):
        left = 0
        others_to_update = 0
        # others_to_update can be a initialized structure, or a new variable
        for right in range(len(s)):
            if conditions:
                # can also be a loop
                update(left)
                update(others_to_update)
            else:
                update(right)
        return others_to_update

    def sliding_window(self, nums: List, goal: int): -> int
        def less_equal_than_goal(self, nums, goal):
            left = 0
            count = 0
            others_to_update
            for right in range(len(nums)):
                # 处理right出现时的各种变化
                while others_to_update > goal:
                    left += 1
                    # 处理left移动后的各种变化
                count += right - left + 1
                # 这一步意为，count计数中当right右移一位后，究竟有多少新增值
            return count
        return less_equal_than_goal(nums, goal) - less_equal_than_goal(nums, goal - 1)

