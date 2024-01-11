class Dequeue:

    def __init__(self):

        self.queue = []

    def size(self):

        return len(self.queue)

    def enterRight(self, item):

        self.queue.append(item)

    def leaveRight(self):

        if self.isEmpty():
            raise IndexError("Attempting to remove item form an empty"
                             "queue")

        return self.queue.pop()

    def enterLeft(self, item):

        self.queue.insert(0, item)

    def leaveLeft(self):

        if self.isEmpty():
            raise IndexError("Attempting to remove item from and empty"
                             "queue")

        return self.queue.pop(0)

    def isEmpty(self):

        return len(self.queue) == 0
