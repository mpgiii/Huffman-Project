from priorityqueue import *


class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        if self.char is not None:
            self.ord = ord(self.char)
        else:
            self.ord = -100000000

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
            pq.enqueue(node, 0 - char_freq)  # negative number because higher freq -> lower priority

    while len(pq) > 1:
        T1 = pq.dequeue()
        T2 = pq.dequeue()
        node = Node(None, (T1.freq + T2.freq), T1, T2)
        pq.enqueue(node, 0 - (T1.freq + T2.freq))

    T = pq.dequeue()

    return T


def get_huffman_code(char, root):
    if root.char == char:
        return ''
    else:
        if root.left is not None:
            code = get_huffman_code(char, root.left)
            if code is not None:
                code = '0' + code
                return code
        if root.right is not None:
            code = get_huffman_code(char, root.right)
            if code is not None:
                code = '1' + code
                return code


def frequency_dict(x):
    frequencies = {}
    for c in x:  # creates a dictionary with all frequencies of characters in given string
        if c not in frequencies:
            frequencies[c] = 0
        frequencies[c] += 1
    return frequencies


def main():
    sent = 'StringTeessttt'
    codes = dict()
    root = huffman(sent)
    for ch in sent:
        codes[ch] = get_huffman_code(ch, root)

    print(codes)


if __name__ == "__main__":
    main()
