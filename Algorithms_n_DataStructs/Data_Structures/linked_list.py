class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.child = None
        self.parent = None


class LinkedList:

    def __init__(self):

        self.head: LinkedNode = None
        self.length = 0

    def add(self, item):

        self.length += 1

        if self.head:
            current: LinkedNode = self.head
            while current.child:
                current = self.head.child

            current.child = LinkedNode(item)
        else:
            self.head = LinkedNode(item)

    def size(self):

        return self.length

    def get(self, index: int):
        """
        Get an item at a given index

        Parameters
        ----------
        arg1: int
            index value of item

        Returns
        -------
        val: any
            Item or value

        """

        if index > -1 and index < self.length:

            # initialise a counter and assign local variable to the head of
            # the linked list
            counter = 0
            current: LinkedNode = self.head
            while current.child:
                if counter == index:
                    return current.val

                # move to the next node and increment counter
                current = current.child
                counter += 1
        else:
            return -1
