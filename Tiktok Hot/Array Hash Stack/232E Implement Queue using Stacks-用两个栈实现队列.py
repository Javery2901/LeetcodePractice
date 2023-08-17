class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B: return self.B.pop()
        if not self.A: return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()


class MyQueue:

    def __init__(self):
        self.write_stack = []
        self.read_stack = []

    def push(self, x: int) -> None:
        self.write_stack.append(x)

    def pop(self) -> int:
        if self.read_stack:
            return self.read_stack.pop()
        while self.write_stack:
            self.read_stack.append(self.write_stack.pop())
        return self.read_stack.pop()

    def peek(self) -> int:
        if self.read_stack:
            return self.read_stack[-1]
        return self.write_stack[0]

    def empty(self) -> bool:
        if self.read_stack or self.write_stack:
            return False
        return True
