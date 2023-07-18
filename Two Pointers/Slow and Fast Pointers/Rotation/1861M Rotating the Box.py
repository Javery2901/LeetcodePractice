from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # two pointers, fast, slow
        # in place
        length = len(box[0])
        for i in range(len(box)):
            fast = 0
            while fast < length and (box[i][fast] == '.' or box[i][fast] == '*'):
                fast += 1  # find the first obstacle or stone first
            if fast == length:
                continue  # means this row does not have stones
            slow = fast  # they are pointing to '#'
            while fast < length:
                if box[i][fast] == '#':
                    fast += 1
                    continue
                elif box[i][fast] == '*':
                    fast += 1
                    while fast < length and box[i][fast] != '#':
                        fast += 1
                    slow = fast
                else:  # box[i][fast] == '.':
                    box[i][fast], box[i][slow] = box[i][slow], box[i][fast]
                    slow += 1
                    fast += 1

        # now we should rotate 90 degrees
        row = len(box)
        col = len(box[0])
        res = [['.'] * row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                res[j][row - i - 1] = box[i][j]
        return res


s = Solution()
box = [["*","#","*",".",".",".","#",".","*","."]]
test = s.rotateTheBox(box)
print(test)