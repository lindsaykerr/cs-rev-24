class Stack:

    def __init__(self):

        self.stack = []

    def push(self, val):

        self.stack.append(val)

    def size(self):
        return len(self.stack)

    def pop(self):

        if self.isEmpty():
            raise IndexError("Attempting to remove from and empty stack")

        return self.stack.pop()

    def peek(self):

        if self.isEmpty():
            return None

        return self.stack[-1]

    def isEmpty(self):

        return len(self.stack) == 0
