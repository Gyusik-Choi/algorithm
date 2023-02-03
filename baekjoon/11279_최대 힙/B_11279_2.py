import sys


class MaxHeap:
    def __init__(self):
        self.arr = [None]
        self.size = 1

    def insert(self, item):
        self.arr.append(item)
        self.size += 1
        idx = self.size - 1

        while idx > 1:
            if self.arr[idx // 2] < self.arr[idx]:
                self.arr[idx // 2], self.arr[idx] = self.arr[idx], self.arr[idx // 2]
                idx = idx // 2
            else:
                break

    def remove(self):
        if self.size > 1:
            self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
            data = self.arr.pop(-1)
            self.size -= 1
            self.max_heapify(1)
            return data
        else:
            print("Nothing to remove")
            return

    def max_heapify(self, idx):
        parent = idx
        left_child = idx * 2
        right_child = idx * 2 + 1

        if left_child < self.size and self.arr[left_child] > self.arr[parent]:
            parent = left_child

        if right_child < self.size and self.arr[right_child] > self.arr[parent]:
            parent = right_child

        if parent != idx:
            self.arr[parent], self.arr[idx] = self.arr[idx], self.arr[parent]
            self.max_heapify(parent)


mh = MaxHeap()
N = int(input())
for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if mh.size == 1:
            sys.stdout.write('0' + '\n')
        else:
            ans = mh.remove()
            sys.stdout.write(str(ans) + '\n')
    else:
        mh.insert(num)
