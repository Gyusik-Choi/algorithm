import sys


class MinHeap:
    def __init__(self):
        self.arr = [None]
        self.size = 1

    def insert(self, item):
        self.arr.append(item)
        self.size += 1
        idx = self.size - 1
        i = idx
        while i > 1:
            if self.arr[i // 2] > self.arr[i]:
                self.arr[i // 2], self.arr[i] = self.arr[i], self.arr[i // 2]
                i = i // 2
            else:
                break

    def remove(self):
        last_idx = self.size - 1
        self.arr[1], self.arr[last_idx] = self.arr[last_idx], self.arr[1]
        item = self.arr.pop()
        self.size -= 1
        self.min_heapify(1)
        return item

    def min_heapify(self, idx):
        parent = idx
        left_child = idx * 2
        right_child = idx * 2 + 1

        if left_child < self.size and self.arr[parent] > self.arr[left_child]:
            parent = left_child

        if right_child < self.size and self.arr[parent] > self.arr[right_child]:
            parent = right_child

        if parent != idx:
            self.arr[idx], self.arr[parent] = self.arr[parent], self.arr[idx]
            self.min_heapify(parent)


mh = MinHeap()
N = int(input())
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(mh.arr) < 2:
            sys.stdout.write(str(0) + '\n')
        else:
            min_num = mh.remove()
            sys.stdout.write(str(min_num) + '\n')
    else:
        mh.insert(num)
