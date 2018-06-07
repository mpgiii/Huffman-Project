from priorityqueue import *


class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.char)

    def __iter__(self):
        yield self.char

        if self.left is not None:
            for elem in self.left:
                yield elem

        if self.right is not None:
            for elem in self.right:
                yield elem


def huffman(x):
    pq = PriorityQueue()    # initialize our priority queue

    freq = frequency_dict(x)

    seen = []
    for char in x:
        if char not in seen:
            seen.append(char)
            char_freq = freq[char]
            node = Node(char, char_freq)     # create a single node binary tree
            pq.enqueue(node, 999 - char_freq)  # 999 - because higher freq -> lower priority

    print(pq)
    while len(pq) > 1:
        T1 = pq.dequeue()
        T2 = pq.dequeue()
        node = Node(None, (T1.freq + T2.freq), T1, T2)
        pq.enqueue(node, 999 - (T1.freq + T2.freq))

    T = pq.dequeue()

    return T

def get_huffman_code(char, root):
    code = []
    if root == char:
        return code.join()
    if root.left == char:
        code.append(1)
    if root.right == char:
        code.append(0)

    return code.join()


def frequency_dict(x):
    frequencies = {}
    for c in x:  # creates a dictionary with all frequencies of characters in given string
        if c not in frequencies:
            frequencies[c] = 0
        frequencies[c] += 1
    return frequencies


def main():
    sent = 'aaaaggcttt'
    codes = dict()
    root = huffman(sent)
    for ch in sent:
        codes[ch] = get_huffman_code(ch, root)

    print(codes)
    print("{'a': '0', 'g': '111', 'c': '110', 't': '10'}")


if __name__ == "__main__":
    main()
