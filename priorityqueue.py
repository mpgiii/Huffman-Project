from linkedlist import *


class PriorityQueue:
    def __init__(self):
        self.items = LinkedList()
        self.frontIdx = 0

    def __compress(self):
        newitems = LinkedList()
        for i in range(self.frontIdx, len(self.items)):
            newitems.append(self.items[i], 0 - self.items[i].freq)

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
        self.items.insert(item, priority)

    def insert(self, item, priority):
        self.items.insert(item, priority)

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
        return len(self.items)


def main():
    PQ = PriorityQueue()
    PQ.enqueue('a', 0)
    print(PQ.isEmpty())
    print(PQ.dequeue())
    print(PQ.isEmpty())


if __name__ == "__main__":
    main()
