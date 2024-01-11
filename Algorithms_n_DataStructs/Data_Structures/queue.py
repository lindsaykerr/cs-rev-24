class Queue:

    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def enter(self, item):
        self.queue.append(item)

    def leave(self):
        if self.isEmpty():
            raise IndexError("Attempting to remove form an item form and empty"
                             "queue")

        return self.queue.pop()

    def isEmpty(self):
        return len(self.queue) == 0
