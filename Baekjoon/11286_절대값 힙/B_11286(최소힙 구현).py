import sys


class MinHeap:
    def __init__(self):
        # 절대값, 기존값
        self.arr = [[None, None]]
        self.size = 1

    def insert_num(self, item):
        self.arr.append(item)
        self.size += 1
        idx = self.size - 1
        while idx > 1:
            # 절대값이 부모 노드가 자식 노드보다 큰 경우
            if self.arr[idx // 2][0] > self.arr[idx][0]:
                self.arr[idx // 2], self.arr[idx] = self.arr[idx], self.arr[idx // 2]
                idx //= 2
            # 부모 노드와 자식 노드의 절대값이 같은 경우
            elif self.arr[idx // 2][0] == self.arr[idx][0]:
                # 기존값이 부모 노드가 자식 노드보다 큰 경우
                if self.arr[idx // 2][1] > self.arr[idx][1]:
                    self.arr[idx // 2], self.arr[idx] = self.arr[idx], self.arr[idx // 2]
                    idx //= 2
                else:
                    break
            else:
                break

    def remove_num(self):
        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
        min_num = self.arr.pop()
        self.size -= 1
        # self.arr 재정렬
        self.min_heapify(1)
        return min_num[1]

    def min_heapify(self, idx):
        parent_idx = idx
        left_child_idx = idx * 2
        right_child_idx = idx * 2 + 1

        # self.size 가 left_child_idx 보다 커야 left_child 가 존재할 수 있다
        # 절대값이 부모 노드가 왼쪽 자식 노드보다 큰 경우
        if self.size > left_child_idx and self.arr[parent_idx][0] > self.arr[left_child_idx][0]:
            parent_idx = left_child_idx
        # 부모 노드의 절대값이 왼쪽 자식노드의 절대값과 같은 경우
        elif self.size > left_child_idx and self.arr[parent_idx][0] == self.arr[left_child_idx][0]:
            # 기존값이 부모 노드가 왼쪽 자식 노드보다 큰 경우
            if self.arr[parent_idx][1] > self.arr[left_child_idx][1]:
                parent_idx = left_child_idx
        
        # self.size 가 right_child_idx 보다 커야 right_child 가 존재할 수 있다
        # 절대값이 부모 노드가 오른쪽 자식 노드보다 큰 경우
        if self.size > right_child_idx and self.arr[parent_idx][0] > self.arr[right_child_idx][0]:
            parent_idx = right_child_idx
        # 부모 노드의 절대값이 오른쪽 자식노드의 절대값과 같은 경우
        elif self.size > right_child_idx and self.arr[parent_idx][0] == self.arr[right_child_idx][0]:
            # 기존값이 부모 노드가 오른쪽 자식 노드보다 큰 경우
            if self.arr[parent_idx][1] > self.arr[right_child_idx][1]:
                parent_idx = right_child_idx

        if parent_idx != idx:
            self.arr[idx], self.arr[parent_idx] = self.arr[parent_idx], self.arr[idx]
            self.min_heapify(parent_idx)


N = int(input())
mh = MinHeap()
for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if mh.size > 1:
            ans_num = mh.remove_num()
            sys.stdout.write(str(ans_num) + "\n")
        else:
            sys.stdout.write(str(0) + "\n")
    else:
        abs_num = abs(num)
        # 절대값, 기존값
        mh.insert_num([abs_num, num])
