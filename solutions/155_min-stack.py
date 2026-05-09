class MinStack:

    def __init__(self):
        self.data = []
        self.min = [1 << 32]

    def push(self, val: int) -> None:
        self.data.append(val)
        prev_min = self.min[-1]
        self.min.append(min(prev_min, val))

    def pop(self) -> None:
        self.min.pop()
        return self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min[-1]
