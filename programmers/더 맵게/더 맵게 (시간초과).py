class MinHeap:
    def __init__(self):
        self.arr = [-1]

    def heap_push(self, item):
        self.arr.append(item)

        i = len(self.arr) - 1

        while i > 1:
            parent_idx = i // 2

            if self.arr[parent_idx] > self.arr[i]:
                self.arr[parent_idx], self.arr[i] = self.arr[i], self.arr[parent_idx]
                i //= 2
            else:
                break

    def heap_pop(self):
        if len(self.arr) <= 1:
            raise Exception()

        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
        min_num = self.arr.pop()
        self.heapify(1)
        return min_num

    def heapify(self, idx):
        parent_idx = idx
        left_child_idx = idx * 2
        right_child_idx = idx * 2 + 1

        if len(self.arr) > left_child_idx and self.arr[parent_idx] > self.arr[left_child_idx]:
            parent_idx = left_child_idx

        if len(self.arr) > right_child_idx and self.arr[parent_idx] > self.arr[right_child_idx]:
            parent_idx = right_child_idx

        if idx != parent_idx:
            self.arr[idx], self.arr[parent_idx] = self.arr[parent_idx], self.arr[idx]
            return self.heapify(parent_idx)


def solution(scoville, k):
    heap = MinHeap()

    for s in scoville:
        heap.heap_push(s)

    cnt = 0

    while len(heap.arr) >= 3:
        first_scoville = heap.heap_pop()
        second_scoville = heap.heap_pop()

        if first_scoville >= k:
            break

        heap.heap_push(first_scoville + (second_scoville * 2))
        cnt += 1

    if len(heap.arr) > 1 and heap.arr[1] < k:
        return -1

    return cnt


print(solution([1, 2, 3, 9, 10, 12], 7))
