class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def two_pointer(ls):
            slow = 0
            for fast in range(len(ls)):
                if ls[fast] != '#':
                    ls[slow] = ls[fast]
                    slow += 1
                else:
                    slow = slow - 1 if slow != 0 else 0
            return ls[:slow]

        ls_s = [i for i in s]
        ls_t = [i for i in t]
        return two_pointer(ls_s) == two_pointer(ls_t)


so = Solution()
s = "a#"
t = "c#"
test = so.backspaceCompare(s, t)
print(test)