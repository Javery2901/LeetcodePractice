class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        while i < len(name) and j < len(typed):
            if typed[j] == name[i]:
                j += 1
                i += 1
            elif i != 0 and typed[j] == name[i - 1]:
                j += 1
            else:
                return False
        return i == len(name) and j == len(typed)


s = Solution()
name = "alex"
typed = "aaleexa"
test = s.isLongPressedName(name, typed)
print(test)