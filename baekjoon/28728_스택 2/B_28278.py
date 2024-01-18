import sys


N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    order = list(map(int, sys.stdin.readline().split()))

    if order[0] == 1:
        stack.append(order[1])
    elif order[0] == 2:
        if not stack:
            sys.stdout.write(str(-1) + "\n")
        else:
            sys.stdout.write(str(stack.pop()) + "\n")
    elif order[0] == 3:
        sys.stdout.write(str(len(stack)) + "\n")
    elif order[0] == 4:
        if not stack:
            sys.stdout.write(str(1) + "\n")
        else:
            sys.stdout.write(str(0) + "\n")
    else:
        if not stack:
            sys.stdout.write(str(-1) + "\n")
        else:
            sys.stdout.write(str(stack[-1]) + "\n")
