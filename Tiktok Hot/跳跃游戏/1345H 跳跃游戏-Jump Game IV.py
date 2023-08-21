import collections
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        count = 0
        target = len(arr) - 1

        al = collections.defaultdict(list)
        for i in range(len(arr)):
            al[arr[i]].append(i)

        queue = collections.deque([0])
        visited = set()
        visited.add(0)
        visited2 = set()  # 用第二个set来存放所有已经被加入过的数字，从而提高速度

        while queue:
            for _ in range(len(queue)):
                pop_index = queue.popleft()
                if pop_index == target:
                    print(visited)
                    return count
                if 0 <= pop_index + 1 < len(arr) and (pop_index + 1) not in visited:
                    queue.append(pop_index + 1)
                    visited.add(pop_index + 1)
                if 0 <= pop_index - 1 < len(arr) and (pop_index - 1) not in visited:
                    queue.append(pop_index - 1)
                    visited.add(pop_index - 1)
                if arr[pop_index] in al and arr[pop_index] not in visited2:
                    for same_num_index in al[arr[pop_index]]:
                        if same_num_index not in visited:
                            queue.append(same_num_index)
                            visited.add(same_num_index)
                    visited2.add(arr[pop_index])
            count += 1


s = Solution()
arr = [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,11]
print(len(arr))
test = s.minJumps(arr)
print(test)