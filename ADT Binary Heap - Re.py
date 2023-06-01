class BinaryHeap:
    def __init__(self):
        self._A = [None]

    def _parent(self, i):
        return i // 2

    def _left(self, i):
        return i * 2

    def _right(self, i):
        return i * 2 + 1

    def _shift_up(self, i):
        if i == 1:
            return
        if self._A[i] > self._A[self._parent(i)]:
            self._A[i], self._A[self._parent(i)] = self._A[self._parent(i)], self._A[i]
            self._shift_up(self._parent(i))

    def _shift_donw(self, i):
        swap_id = i
        if self._left(i) < len(self._A) and self._A[i] < self._A[self._left(i)]:
            swap_id = self._left(i)
        if self._right(i) < len(self._A) and self._A[i] < self._A[self._right(i)]:
            swap_id = self._right(i)
        if swap_id != i:
            self._A[i], self._A[swap_id] = self._A[swap_id], self._A[i]
            self._shift_donw(swap_id)

    def push(self, x):
        self._A.append(x)
        self._shift_up(len(self._A)-1)

    def pop(self):
        if self.empty():
            return
        self._A[1], self._A[-1] = self._A[-1], self._A[1]
        self._A.pop()
        self._shift_donw(1)

    def top(self):
        return self._A[1]

    def empty(self):
        return len(self._A) == 1

    def size(self):
        return len(self._A)-1

print("Our own Binary Heap")
pq = BinaryHeap()
print(pq.empty())

