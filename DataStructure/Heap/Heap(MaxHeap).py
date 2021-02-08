class MaxHeap:
    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)
        i = len(self.data) - 1
        while i > 1:
            if self.data[i // 2] < self.data[i]:
                self.data[i // 2], self.data[i] = self.data[i], self.data[i // 2]
                i = i // 2
            else:
                break

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.max_heapify(1)
        else:
            data = None
        return data

    def max_heapify(self, i):
        parent = i
        left_child = 2 * i
        right_child = 2 * i + 1
        if left_child < len(self.data) and self.data[i] < self.data[left_child]:
            parent = left_child

        if right_child < len(self.data) and self.data[parent] < self.data[right_child]:
            smallest = right_child

        if parent != i:
            self.data[i], self.data[parent] = self.data[parent], self.data[i]
            self.max_heapify(parent)

    def __str__(self):
        lst = []
        for node in self.arr:
            lst.append(str(node))
        return ' '.join(lst)


mh = MaxHeap()
mh.insert(1)
mh.insert(2)
mh.insert(3)
mh.insert(4)
mh.insert(5)
mh.insert(6)
mh.insert(7)
mh.insert(8)
mh.insert(9)
mh.insert(10)
print(mh.remove())
print(mh)


# 참고
# https://m.blog.naver.com/PostView.nhn?blogId=leeinje66&logNo=221622360256&proxyReferer=https:%2F%2Fwww.google.com%2F
# https://yabmoons.tistory.com/374
