class Dequeue:

    def __init__(self):

        self.queue = []
        self.length = 0

    def size(self):

        return self.length

    def enterRight(self, item):

        self.length += 1
        self.queue.append(item)

    def leaveRight(self):

        if self.length-1 == -1:
            raise IndexError("Attempting to remove item form an empty"
                             "queue")
        self.length -= 1

        return self.queue.pop()

    def enterLeft(self, item):

        self.length += 1
        self.queue.insert(0, item)

    def leaveLeft(self):

        if self.length-1 == -1:
            raise IndexError("Attempting to remove item from and empty"
                             "queue")
        self.length -= 1

        return self.queue.pop(0)

    def isEmpty(self):

        return self.length == 0
