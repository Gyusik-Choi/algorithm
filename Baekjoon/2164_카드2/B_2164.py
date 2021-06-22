from collections import deque


N = int(input())
deq = deque()
for i in range(1, N + 1):
    deq.append(i)

deq_size = N
if deq_size > 1:
    while True:
        deq.popleft()
        deq_size -= 1
        if deq_size > 1:
            front_num = deq.popleft()
            deq.append(front_num)
        else:
            break

print(*deq)
