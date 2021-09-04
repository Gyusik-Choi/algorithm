# 힙은 부모 노드와 자식 노드의 정렬을 하고 자식 노드 간에는 정렬이 수행되지 않아서 완전한 정렬 상태가 아니다
# 1번 인덱스 요소가 최소힙인지, 최대힙인지에 따라 맞는 값이 찾아지는지에 집중하면 된다


class MinHeap:
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
                idx //= 2
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

        # 왼쪽 자식노드가 있는지 확인
        if self.size > 2 and self.arr[parent] > self.arr[left_child]:
            parent = left_child

        # 오른쪽 자식노드가 있는지 확인
        if self.size > 3 and self.arr[parent] > self.arr[right_child]:
            parent = right_child

        if idx != parent:
            self.arr[idx], self.arr[parent] = self.arr[parent], self.arr[idx]
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
# https://m.blog.naver.com/PostView.nhn?blogId=leeinje66&logNo=221622360256&proxyReferer=https:%2F%2Fwww.google.com%2F
