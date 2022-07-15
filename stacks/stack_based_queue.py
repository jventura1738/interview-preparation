# Justin Ventura

class MyQueue:

    def __init__(self):
        self.instack, self.outstack = list(), list()

    def push(self, x: int) -> None:
        self.instack.append(x)

    def pop(self) -> int:
        # Edge case:
        if len(self.instack) == 0:
            return None

        return self.reshape('pop')

    def peek(self) -> int:
        # Edge case:
        if len(self.instack) == 0:
            return None

        return self.reshape('peek')

    def reshape(self, op: str) -> int:
        # Shape outstack:
        while self.instack:
            self.outstack.append(self.instack.pop())

        # Pop off the end:
        if op == 'peek':
            value = self.outstack[-1]
        elif op == 'pop':
            value = self.outstack.pop()

        # Shape instack:
        while self.outstack:
            self.instack.append(self.outstack.pop())

        return value

    def empty(self) -> bool:
        return len(self.instack) == 0


if __name__ == '__main__':
    queue = MyQueue()
    for i in range(5):
        queue.push(i)
    res = [queue.pop() for _ in range(5)]
    assert(res == [0, 1, 2, 3, 4])
