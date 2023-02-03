from collections import deque
import sys


N = int(input())
q = deque()
for i in range(N):
    order = sys.stdin.readline().strip()
    if "push" in order:
        order, num = order.split()
        num = int(num)
        q.append(num)
    else:
        if order == 'front':
            if q:
                sys.stdout.write(str(q[0]) + "\n")
            else:
                sys.stdout.write(str(-1) + "\n")
        elif order == 'back':
            if q:
                sys.stdout.write(str(q[-1]) + "\n")
            else:
                sys.stdout.write(str(-1) + "\n")
        elif order == 'size':
            sys.stdout.write(str(len(q)) + "\n")
        elif order == 'empty':
            if q:
                sys.stdout.write(str(0) + "\n")
            else:
                sys.stdout.write(str(1) + "\n")
        # pop
        else:
            if q:
                pop_num = q.popleft()
                sys.stdout.write(str(pop_num) + "\n")
            else:
                sys.stdout.write(str(-1) + "\n")