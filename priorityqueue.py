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
            raise RuntimeError("Attempt to dequeue an empty queue")

        # When queue is half full, compress it. This
        # achieves an amortized complexity of O(1) while
        # not letting the list continue to grow unchecked.
        if self.frontIdx * 2 > len(self.items):
            self.__compress()

        item = self.items[self.frontIdx]
        del self.items[0]
        return item[0]

    def enqueue(self, item, priority):
        def getpriority(elem):
            return elem[1]

        def breakties(elem):
            try:
                return elem[0].ord
            except:
                return 0

        self.items.insert(0, (item, priority))
        self.items = sorted(self.items, key=breakties)
        self.items = sorted(self.items, key=getpriority, reverse=True)

    def front(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to access front of empty queue")

        return self.items[self.frontIdx][0]

    def isEmpty(self):
        return self.frontIdx == len(self.items)

    def clear(self):
        self.items = LinkedList()
        self.frontIdx = 0

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return str(len(self.items))


def main():
    pq = PriorityQueue()
    pq.enqueue('a', 0)
    print(pq.front(), 'a')
    pq.enqueue('b', 5)
    print(pq.front(), 'b')
    pq.enqueue('z', 100)
    print(pq.front(), 'z')
    pq.enqueue('ZZ', -1)
    print(pq.front(), 'z')


if __name__ == "__main__":
    main()