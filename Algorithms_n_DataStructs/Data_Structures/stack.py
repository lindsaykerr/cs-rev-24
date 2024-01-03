class Stack:

    def __init__(self):

        self.stack = []
        # This stack uses a verbose way of calculating size,
        # through incrementation and decrementation. In practise the list
        # length should be used.
        self.length = 0

    def push(self, val):

        self.stack.append(val)
        self.length += 1

    def size(self):
        # return len(self.stack)
        return self.length

    def pop(self):

        if self.length-1 == -1:
            raise IndexError("Attempting to remove from and empty stack")

        self.length -= 1
        return self.stack.pop()

    def peek(self):

        if self.length == 0:
            return None

        return self.stack[self.length-1]

    def isEmpty(self):

        return self.length == 0
