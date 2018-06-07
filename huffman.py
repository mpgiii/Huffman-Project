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
        node = Node(freq, char, None, None)
        pq.enqueue(node, 999 - freq)

    while len(pq) > 1:
        T1 = pq.dequeue()
        T2 = pq.dequeue()
        node = Node((T1.freq + T2.freq), None, T1, T2)
        pq.enqueue(node, 999 - (T1.freq + T2.freq))

    T = pq.dequeue()

    return T


def frequency(x, c):
    count = 0
    for char in x:
        if char == c:
            count += 1
    return count


def main():
    sent = 'aaaaggccttt'; codes = dict(); root = huffman(sent)
    for ch in sent:
        codes[ch] = get_huffman_code(ch, root)

    print(codes)
    print("{'a': '0', 'g': '111', 'c': '110', 't': '10'}")

if __name__ == "__main__":
    main()
