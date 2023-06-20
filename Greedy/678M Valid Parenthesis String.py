class Solution:
    def checkValidString(self, s: str) -> bool:  # optimal: O(n), O(1)
        # idea: use two pointers to update the number of "(", left_max, left_min

        left_min = 0
        left_max = 0
        for i in s:
            if i == '(':
                left_max += 1
                left_min += 1
            elif i == ')':
                left_max -= 1
                left_min -= 1
            else:
                left_max += 1
                left_min -= 1
            if left_max < 0:
                return False
            if left_min < 0:
                left_min = 0  # 如果* 和）多余（， left_min 会小于0
                # 两种情况，当）多余（时，left_max已经返回False
                # 因此只可能是存在*，使得*+）>(， 这种情况下，left_min应当记为0
                # 即一部分* 当作）处理，一部分*当作‘’处理。left_min 存在的最小值是0
        return left_min == 0  # 若left_min > 0, 意为（的数量在遍历完后一定会依然存在，无法被*）消除，故为False




so = Solution()
s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
test = so.checkValidString(s)
print(test)
"""
'(((((**(********((*(((((****'
'****((((((****'
"""

