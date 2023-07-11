class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return str(0)
        res = 0
        for i in range(len(num1)):
            n1 = int(num1[i]) * 10 ** (len(num1) - i - 1)
            for j in range(len(num2)):
                res += n1 * int(num2[j]) * 10 ** (len(num2) - j -1)
        return str(res)

        # 对其它语言来说 可能会出现32位，64位溢出情况

    def multiply_optimal(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return str(0)
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i + j] += int(num1[i]) * int(num2[j])
                res[i + j + 1] += res[i + j] // 10
                res[i + j] = res[i + j] % 10

        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return ''.join(res)


s = Solution()
num1 = "123"
num2 = "456"
test = s.multiply_optimal(num1, num2)
print(test)