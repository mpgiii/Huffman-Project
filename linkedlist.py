class LinkedList:
    # The __Node class is used internally by the LinkedList class. It is
    # invisible from outside this class due to the two underscores
    # that precede the class name. Python mangles names so that they
    # are not recognizable outside the class when two underscores
    # precede a name but aren't followed by two underscores at the
    # end of the name (i.e. an operator name).
    class __Node:
        def __init__(self, item, priority=0, next=None):
            self.item = item
            self.priority = priority
            self.next = next

        def getItem(self):
            return self.item

        def getNext(self):
            return self.next

        def getPriority(self):
            return self.priority

        def setItem(self, item):
            self.item = item

        def setNext(self, next):
            self.next = next

    def __init__(self, contents=[]):
        # Here we keep a reference to the first node in the linked list
        # and the last item in the linked list. The both point to a
        # dummy node to begin with. This dummy node will always be in
        # the first position in the list and will never contain an item.
        # Its purpose is to eliminate special cases in the code below.
        self.first = LinkedList.__Node(None, None, None)
        self.last = self.first
        self.numItems = 0

        for e in contents:
            self.append(e)

    def __getitem__(self, index):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

            return cursor.getItem()

        raise IndexError("LinkedList index out of range")

    def __setitem__(self, index, val):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

            cursor.setItem(val)
            return

        raise IndexError("LinkedList assignment index out of range")

    def insert(self, item, priority):
        newNode = LinkedList.__Node(item, priority)
        prev = None
        curr = self.first
        if self.numItems == 0:
            self.first = newNode
            self.numItems += 1
            return
        while curr is not None and newNode.priority < curr.priority:
            prev = curr
            curr = curr.next
        if prev is None:
            newNode.next = self.first
            self.first = newNode
            self.numItems += 1
        else:
            prev.next = newNode
            newNode.next = curr
            self.numItems += 1


    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Concatenate undefined for " + \
                            str(type(self)) + " + " + str(type(other)))

        result = LinkedList()

        cursor = self.first.getNext()

        while cursor is not None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()

        cursor = other.first.getNext()

        while cursor is not None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()

        return result

    def __contains__(self, item):
        # This is left as an exercise for the reader.
        index = self.first
        while index is not None:
            if index.item == item:
                return True
            index = index.next
        return False

    def __delitem__(self, index):
        # This is left as an exercise for the reader.
        current = -1
        x = self.first
        while current < index:
            prev = x
            x = x.next
            current += 1
            if current == index:
                prev.next = x.next
        self.numItems -= 1

    def __eq__(self, other):
        if type(other) != type(self):
            return False

        if self.numItems != other.numItems:
            return False

        cursor1 = self.first.getNext()
        cursor2 = other.first.getNext()
        while cursor1 is not None:
            if cursor1.getItem() != cursor2.getItem():
                return False
            cursor1 = cursor1.getNext()
            cursor2 = cursor2.getNext()

        return True

    def __iter__(self):  ###
        # This is left as an exercise for the reader.
        current = self.first
        while current is not None:
            yield current.item
            yield current.priority
            current = current.next

    def __len__(self):
        # This is left as an exercise for the reader.
        return self.numItems

    def append(self, item, priority):
        node = LinkedList.__Node(item, priority)
        self.last.setNext(node)
        self.last = node
        self.numItems += 1

    def __str__(self):
        # This is left as an exercise for the reader.
        return str(list(self))

    def __repr__(self):
        # This is left as an exercise for the reader.
        return str(list(self))


def main():
    pass


if __name__ == "__main__":
    main()