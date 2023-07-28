import collections
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        # bfs
        visited = {(sr, sc)}
        original_color = image[sr][sc]
        queue = collections.deque([(sr, sc)])
        while queue:
            row, col = queue.popleft()
            image[row][col] = color
            for r, c in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                if 0 <= r < len(image) and 0 <= c < len(image[0]):
                    if (r, c) not in visited and image[r][c] == original_color:
                        visited.add((r, c))
                        queue.append((r, c))
        return image


s = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
print(s.floodFill(image, sr, sc, color))