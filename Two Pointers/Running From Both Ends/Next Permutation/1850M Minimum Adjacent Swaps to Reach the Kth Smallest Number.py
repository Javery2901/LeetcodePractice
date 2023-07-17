class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        # brutal force
        # everytime do the next permutation: O(n) using two pointers, so overall is O(n * k)
        ls = list(num)
        for _ in range(k):
            i = j = len(ls) - 1
            while i > 0 and ls[i - 1] >= ls[i]:
                i -= 1  # find the first index that smaller than index + 1
            while j > i and ls[i - 1] >= ls[j]:
                j -= 1  # find the first index that bigger than index - 1
            # eg [1,3,2] -> index i = 1, index j = 2
            # swap i - 1, j first -> [2,3,1] and then reverse -> [2, 1, 3]
            ls[j], ls[i - 1] = ls[i - 1], ls[j]
            ls[i:] = ls[len(ls) - 1: i - 1: -1]

        original = list(num)
        res = 0
        for i in range(len(ls)):
            if ls[i] != original[i]:
                for j in range(i + 1, len(ls)):
                    if ls[i] == original[j]:
                        res += j - i
                        original = list(original[:i]) + list(original[j]) + list(original[i: j]) + list(original[j + 1:])
                        break
        return res


s = Solution()
num = "5489355142"
k = 4
test = s.getMinSwaps(num,k)
print(test)

"""
num = "11112", k = 4  # 4

num = "00123", k = 1  # 1
"""