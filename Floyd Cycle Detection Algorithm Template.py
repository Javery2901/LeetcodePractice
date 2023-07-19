"""
Floyd判圈算法(Floyd Cycle Detection Algorithm),又称龟兔赛跑算法(Tortoise and Hare Algorithm)。
可以在有限状态机、迭代函数或者链表上判断是否存在环，求出该环的起点与长度的算法。
time complexity: O(m+n) m为起点到环起点的长度，n为环的长度
space complexity: O(1)

算法：
    初始状态下，假设已知某个起点节点为节点S。现设两个指针fast和slow，将它们均指向S。
    同时让fast和slow往前推进，但是二者的速度不同：slow每前进1步，fast前进2步。
    当fast无法前进，即到达某个没有后继的节点时，就可以确定从S出发不会遇到环。
    反之当fast与slow再次相遇时，就可以确定从S出发一定会进入某个环.
    为了求出环的起点，只要令slow仍位于节点M，而令fast返回起点节点S。随后，同时让fast和slow以步伐1步往前推进。
    持续该过程直至两指针再一次相遇，设此次相遇时位于同一节点P，则节点P即为从节点S出发所到达的环C的第一个节点，即环C的一个起点。
证明过程：https://blog.csdn.net/fuhuixin7497/article/details/78157306/
"""
"""
以 leetcode 287为典型. Find the Duplicate Number
以 leetcode 141为典型，Linked List Cycle
以 leetcode 142为典型，Linked List Cycle II
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = nums[nums[0]], nums[0]
        while fast != slow:
            print(slow, fast)
            slow = nums[slow]
            fast = nums[nums[fast]]
        print(slow, fast)
        print()
        fast = 0
        while fast != slow:
            print(slow, fast)
            slow = nums[slow]
            fast = nums[fast]
        return fast


s = Solution()
nums = [2, 5, 9, 6, 9, 3, 8, 4, 7, 1]
test = s.findDuplicate(nums)
print(test)
