from linkedlist import *


class PriorityQueue:
    def __init__(self):
        self.items = LinkedList()
        self.frontIdx = 0

    def __compress(self):
        newitems = LinkedList()
        for i in range(self.frontIdx, len(self.items)):
            newitems.append(self.items[i])

        self.items = newitems
        self.frontIdx = 0

    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to dequeue an empty priority queue")

        # When queue is half full, compress it. This
        # achieves an amortized complexity of O(1) while
        # not letting the list continue to grow unchecked.
        if self.frontIdx * 2 > len(self.items):
            self.__compress()

        item = self.items.first.item
        self.frontIdx += 1
        return item

    def enqueue(self, item, priority):
        for i in len(self.items):
            if len(self.items[i]) > 1:
                if priority > self.items[i][1]:
                    self.items.insert(i, (item, priority))
            else:
                self.items.insert(len(self.items[i]), (item, priority))

    def insert(self, item, priority):
        for i in len(self.items):
            if len(self.items[i]) > 1:
                if priority > self.items[i][1]:
                    self.items.insert(i, (item, priority))
            else:
                self.items.insert(len(self.items[i]), (item, priority))

    def front(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to access front of empty queue")

        return self.items.first.item

    def isEmpty(self):
        return self.frontIdx == len(self.items)

    def clear(self):
        self.items = LinkedList()
        self.frontIdx = 0

    def __len__(self):
        return self.items.numItems


def main():
    PQ = PriorityQueue()
    PQ.enqueue('a', 0)
    print(PQ.isEmpty())
    print(PQ.dequeue())
    print(PQ.isEmpty())


if __name__ == "__main__":
    main()
