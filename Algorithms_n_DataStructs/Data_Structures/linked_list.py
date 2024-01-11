class LinkedNode:

    def __init__(self, val):
        self.val = val
        self.child = None
        self.parent = None


class LinkedList:

    def __init__(self):
        self.head: LinkedNode = None
        self.size = 0

    def append(self, item):
        """
        Append an item to the end of Linked list

        Parameters
        ----------
        item: any
            the value of item to be added to the Linked list
        """

        if self.head:
            current = self._to(self.size-1)
            current[0].child = LinkedNode(item)
        else:
            self.head = LinkedNode(item)

        self.size += 1

    def insert(self, indx, item):
        """
        Inserts and item into a linked list at position indx, if indx is a
        value which is not with in the range of the Linked list length then
        the item will be added to the end of the list

        Parameters
        ----------
        indx: int
            The index of the linked list item
        item: any
            the value or object stored within the linked list
        """

        if indx < 0 or indx > self.size - 1:
            self.append(item)
            return

        nodes = self._to(indx)

        current, parent = nodes[0], nodes[1]
        temp = current
        if self.head == current:
            self.head = LinkedNode(item)
            self.head.child = temp
        else:
            parent.child = LinkedNode(item)
            parent.child.child = temp

        self.size += 1

    def length(self):
        """
        Get the length of the linked list

        Returns
        -------
        int
            The length of the Linked list
        """

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

            current = self._to(index)

            return current[0].val
        else:
            raise IndexError("Index out of bounds")

    def has(self, item):
        """
        Check if an item is within the linked list

        Parameters
        ----------
        item: any
            The item to be searched for
        """

        indx = self._findIndx(item)
        if indx == -1:
            return False
        else:
            return True

    def index(self, item):
        """
        Return the index value of an item in the list

        Parameters
        ----------
        item: any
            The index of an linked list item
        """

        return self._findIndx(item)

    def isEmpty(self):
        """
        Check if the device is linked list is empty

        Returns
        -------
        bool
            True if the list is empty false otherwise
        """

        return self.size == 0

    def pop(self, pos=None):
        """
        Remove an item from the end of the linked list

        Returns
        -------
        item: any
            A value or object within a list
        """

        if self.size == 0:
            raise OverflowError("Cannot remove from and empty linked list")

        indx = self.size-1

        if isinstance(pos, int) and pos > -1 and pos < self.size:
            indx = pos

        nodes = self._to(indx)
        current, parent = nodes[0], nodes[1]

        val = current.val
        if current == self.head:
            self.head = current.child
        else:
            parent.child = current.child
        del current

        self.size -= 1

        return val

    def add(self, item):
        """
        Adds an item to the start of the linked list

        Parameters
        ----------
        item: any
            value or object to be added
        """

        self.size += 1

        if self.head is not None:
            temp = self.head
            self.head = LinkedNode(item)
            self.head.child = temp
        else:
            self.head = LinkedNode(item)

    # HELPER METHODS

    def _to(self, pos):
        """
        Goes up to a point in the linked list, then returns the current and
        parent node
        """
        current: LinkedNode = self.head
        parent = self.head
        count = 0
        while count < pos and current.child:
            parent = current
            current = current.child
            count += 1

        if pos != count:
            raise OverflowError("Invalid item postion on linked list")
        else:
            return (current, parent)

    def _findIndx(self, item):
        """
        Finds the index of an node item in the list return -1 if nothing
        is found
        """
        current: LinkedNode = self.head
        indx_counter = 0
        while current.child and item != current.val:
            current = current.child
            indx_counter += 1

        if current.val != item:
            return -1
        else:
            return indx_counter

    def printOut(self):
        """
        Prints out the items within the list
        """

        current = self.head
        list = '['
        while current.child:
            list = list + str(current.val) + "->"
            current = current.child

        list = list + str(current.val) + ']'
        print(list)
