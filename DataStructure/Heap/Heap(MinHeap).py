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
mh.remove()
mh.remove()
mh.remove()
mh.remove()
mh.remove()
mh.remove()
mh.remove()
mh.remove()
mh.remove()
mh.remove()
print(mh)

# 참고
# https://m.blog.naver.com/PostView.nhn?blogId=leeinje66&logNo=221622360256&proxyReferer=https:%2F%2Fwww.google.com%2F
# https://yabmoons.tistory.com/374