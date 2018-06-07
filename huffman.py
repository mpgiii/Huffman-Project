from priorityqueue import *


class Node:
   def __init__(self, freq, char, left, right):
      self.freq = freq
      self.char = char
      self.left = left
      self.right = right


def huffman(x):
    pq = PriorityQueue()
    for char in x:
        freq = frequency(x, char)
        pq.enqueue(Node(freq, char, None, None), freq)

    while len(pq) > 1:
        T1 = pq.dequeue()
        T2 = pq.dequeue()
        pq.insert()

def frequency(x, c):
    count = 0
    for char in x:
        if char == c:
            count += 1
    return count


def main():
    pass


if __name__ == "__main__":
    main()
