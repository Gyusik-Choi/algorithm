class MinHeap:
    def __init__(self):
        self.arr = [None]
        self.size = 1

    def insert(self, item):
        self.arr.append(item)
        self.size += 1
        idx = self.size - 1
        while idx > 1:
            if self.arr[idx // 2] > self.arr[idx]:
                self.arr[idx // 2], self.arr[idx] = self.arr[idx], self.arr[idx // 2]
                idx = idx // 2
            else:
                break

    def remove(self):
        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
        min_num = self.arr.pop()
        self.size -= 1
        self.min_heapify(1)
        return min_num

    def min_heapify(self, idx):
        parent = idx
        left_child = idx * 2
        right_child = idx * 2 + 1

        if left_child < self.size and self.arr[left_child] < self.arr[parent]:
            parent = left_child

        if right_child < self.size and self.arr[right_child] < self.arr[parent]:
            parent = right_child

        if parent != idx:
            self.arr[parent], self.arr[idx] = self.arr[idx], self.arr[parent]
            self.min_heapify(parent)


mh = MinHeap()
sorted_arr = []
arr = [2, 1, 5, 3, 4, 7, 6]
for i, n in enumerate(arr):
    mh.insert(n)

while mh.size > 1:
    num = mh.remove()
    sorted_arr.append(num)

print(sorted_arr)
