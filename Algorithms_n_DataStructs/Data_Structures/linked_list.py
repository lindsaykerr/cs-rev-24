class LinkedNode:

    def __init__(self, val):
        self.val = val
        self.child = None
        self.parent = None


class LinkedList:

    def __init__(self):
        self.head: LinkedNode = None
        self.size = 0

    def add(self, item):

        self.size += 1

        if self.head:
            current: LinkedNode = self.head
            while current.child:
                current = current.child

            current.child = LinkedNode(item)
        else:
            self.head = LinkedNode(item)

    def insert(self, indx, item):

        if indx < 0 or indx > self.size - 1:
            self.add(item)
            return

        counter = 0
        current: LinkedNode = self.head
        parent = self.head
        while current.child:
            if indx == counter:
                break
            counter += 1
            current = current.child
            parent = current

        # break the link insert new item and reforms the link again
        temp = current
        if self.head == current:
            self.head = LinkedNode(item)
            self.head.child = temp
        else:
            parent.child = LinkedNode(item)
            parent.child.child = temp

        self.size += 1

    def length(self):

        return self.size

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

        if index > -1 and index < self.size:

            # initialise a counter and assign linked list head to a temp
            # reference variable
            counter = 0
            current: LinkedNode = self.head
            while current.child:
                if counter == index:
                    break
                # move to the next node and increment counter
                current = current.child
                counter += 1
            return current.val
        else:
            raise IndexError("Index out of bounds")

    def has(self, item):
        current: LinkedNode = self.head
        while current.child:
            if current.val == item:
                break
            current = current.child

        if current.val == item:
            return True
        else:
            return False

    def index(self, item):
        counter = 0
        current: LinkedNode = self.head
        while current.child:
            if current.val == item:
                break
            current = current.child
            counter += 1

        if current.val == item:
            return counter
        else:
            return -1

    def isEmpty(self):

        return self.size == 0

    def printOut(self):
        current = self.head
        list = '['
        while current.child:
            list = list + str(current.val) + "->"
            current = current.child

        list = list + str(current.val) + ']'
        print(list)

    def pop(self):
        if self.size == 0:
            raise OverflowError("Cannot remove from and empty linked list")

        current: LinkedNode = self.head
        parent = self.head
        while current.child:
            parent = current
            current = current.child

        val = current.val
        parent.child = None
        del current

        self.size -= 1
        
        return val

