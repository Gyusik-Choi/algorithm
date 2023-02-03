from collections import deque
import sys


def find_closer_side(deq_idx):
    length = len(deq)
    # 오른쪽으로 빼기
    if length // 2 < deq_idx:
        return 1
    # 왼쪽으로 빼기
    return 0


def find_idx(num):
    return deq.index(num)


def pop_number(n):
    global cnt
    idx = find_idx(n)
    side = find_closer_side(idx)
    if side:
        while deq[0] != n:
            cnt += 1
            popped_number = deq.pop()
            deq.appendleft(popped_number)
    else:
        while deq[0] != n:
            cnt += 1
            popped_number = deq.popleft()
            deq.append(popped_number)

    deq.popleft()
    return


N, M = map(int, sys.stdin.readline().split())
deq = deque()
for i in range(1, N + 1):
    deq.append(i)

cnt = 0
numbers = list(map(int, sys.stdin.readline().split()))
for number in numbers:
    if deq[0] == number:
        deq.popleft()
        continue
    else:
        pop_number(number)

sys.stdout.write(str(cnt))
