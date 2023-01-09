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
                idx //= 2
            else:
                break

    def remove(self):
        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
        self.size -= 1
        min_val = self.arr.pop()
        self.min_heapify(1)
        return min_val

    def min_heapify(self, idx):
        parent_idx = idx
        left_child_idx = idx * 2
        right_child_idx = idx * 2 + 1

        # self.size 보다 작아야 존재 가능
        if left_child_idx < self.size and self.arr[parent_idx] > self.arr[left_child_idx]:
            parent_idx = left_child_idx

        # self.size 보다 작아야 존재 가능
        if right_child_idx < self.size and self.arr[parent_idx] > self.arr[right_child_idx]:
            parent_idx = right_child_idx

        if idx != parent_idx:
            self.arr[idx], self.arr[parent_idx] = self.arr[parent_idx], self.arr[idx]
            self.min_heapify(parent_idx)

    def __str__(self):
        lst = []
        for node in self.arr:
            lst.append(str(node))
        return ' '.join(lst)


mh = MinHeap()
mh.insert(10)
mh.insert(9)
mh.insert(8)
mh.insert(7)
mh.insert(6)
mh.insert(5)
mh.insert(4)
mh.insert(3)
mh.insert(2)
mh.insert(1)
print(mh)
print(mh.remove())
print(mh.remove())
print(mh.remove())
print(mh.remove())
print(mh.remove())
print(mh.remove())
print(mh.remove())
print(mh.remove())
print(mh.remove())
print(mh.remove())
print(mh)

# 참고
# https://gmlwjd9405.github.io/2018/05/10/data-structure-heap.html
# https://m.blog.naver.com/leeinje66/221622360256
