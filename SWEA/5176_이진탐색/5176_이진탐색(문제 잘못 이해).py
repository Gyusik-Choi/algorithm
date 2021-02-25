import math


def make_tree(idx, num, c):
    if c > 0:
        left_child_idx = idx - c
        right_child_idx = idx + c
        arr[left_child_idx] = num * 2
        arr[right_child_idx] = num * 2 + 1
        make_tree(left_child_idx, arr[left_child_idx], c // 2)
        make_tree(right_child_idx, arr[right_child_idx], c // 2)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    # 0번 인덱스는 None 처럼 취급하고 진행 1번 부터 실제 값 담는다
    log_num = math.floor(math.log2(N)) + 1
    full_index = 2 ** log_num
    arr = [0] * full_index
    middle_index = 2 ** log_num // 2
    arr[middle_index] = 1
    cnt = middle_index // 2
    make_tree(middle_index, 1, cnt)
    print(arr)

