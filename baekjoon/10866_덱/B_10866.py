from collections import deque
import sys


N = int(input())
deq = deque()
for i in range(N):
    order = sys.stdin.readline().rstrip()
    if "push" in order:
        order, num = order.split()
        if order == "push_front":
            deq.appendleft(num)
        else:
            deq.append(num)
    else:
        if order == "pop_front":
            if deq:
                pop_num = deq.popleft()
                sys.stdout.write(str(pop_num) + "\n")
            else:
                sys.stdout.write(str(-1) + "\n")
        elif order == "pop_back":
            if deq:
                pop_num = deq.pop()
                sys.stdout.write(str(pop_num) + "\n")
            else:
                sys.stdout.write(str(-1) + "\n")
        elif order == "size":
            sys.stdout.write(str(len(deq)) + "\n")
        elif order == "empty":
            if deq:
                sys.stdout.write(str(0) + "\n")
            else:
                sys.stdout.write(str(1) + "\n")
        elif order == "front":
            if deq:
                sys.stdout.write(str(deq[0]) + "\n")
            else:
                sys.stdout.write(str(-1) + "\n")
        else:
            if deq:
                sys.stdout.write(str(deq[-1]) + "\n")
            else:
                sys.stdout.write(str(-1) + "\n")
