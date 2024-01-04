class Queue:

    def __init__(self):
        self.queue = []
        self.length = 0

    def size(self):
        return self.length

    def enter(self, item):
        self.length += 1
        self.queue.append(item)

    def leave(self):
        if self.length-1 == -1:
            raise IndexError("Attempting to remove form an item form and empty"
                             "queue")
        self.length -= 1

        return self.queue.pop()

    def isEmpty(self):
        return self.length == 0
