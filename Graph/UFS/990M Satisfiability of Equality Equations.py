from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # 策略，创建ls_equal
        # 先遍历整个equations，每拿到两个数，若==，将其union在ls_equal中,
        # 再遍历整个equations，每拿到两个数，若!=，判断其find(x) == find(y)，若是，返回False

        ls_equal = [i for i in range(26)]

        def find(x, ls):
            if x == ls[x]:
                return x
            cur = x
            while cur != ls[cur]:
                cur = ls[cur]
            return cur

        def union(x, y, ls):
            x_parent = find(x, ls)
            y_parent = find(y, ls)
            if x_parent == y_parent:
                return
            ls[x_parent] = y_parent
            return

        for equation in equations:
            first, second = ord(equation[0]) - 97, ord( equation[-1]) - 97
            # convert them into int
            # print(first, second)
            if equation[1] == '=':
                union(first, second, ls_equal)

        for equation in equations:
            first, second = ord(equation[0]) - 97, ord(equation[-1]) - 97
            # convert them into int
            # print(first, second)
            if equation[1] == '!':
                if find(first, ls_equal) == find(second, ls_equal):
                    return False
        return True


s = Solution()
equations = ["a==b","b!=c","c==a"]
test = s.equationsPossible(equations)
print(test)