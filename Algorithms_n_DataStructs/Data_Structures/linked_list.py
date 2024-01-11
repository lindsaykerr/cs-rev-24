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

        self.size += 1

        if self.head:
            current: LinkedNode = self.head
            while current.child:
                current = current.child

            current.child = LinkedNode(item)
        else:
            self.head = LinkedNode(item)

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
        """
        Check if an item is within the linked list

        Parameters
        ----------
        item: any
            The item to be searched for
        """

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
        """
        Return the index value of an item in the list

        Parameters
        ----------
        item: any
            The index of an linked list item
        """

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

        counter = 0
        current: LinkedNode = self.head
        parent = self.head
        while counter < indx:
            counter += 1
            parent = current
            current = current.child

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
