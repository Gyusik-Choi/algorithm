import sys


N = int(input())
arr = []
size = 0
for i in range(N):
    order = sys.stdin.readline().strip()

    if "push" in order:
        num = order[5:]
        arr.append(num)
        size += 1

    elif order == "pop":
        if size == 0:
            sys.stdout.write('-1' + '\n')
        else:
            num = arr.pop()
            sys.stdout.write(str(num) + '\n')
            size -= 1

    elif order == "size":
        sys.stdout.write(str(size) + '\n')

    elif order == "empty":
        if size == 0:
            sys.stdout.write('1' + '\n')
        else:
            sys.stdout.write('0' + '\n')

    elif order == "top":
        if size == 0:
            sys.stdout.write('-1' + '\n')
        else:
            sys.stdout.write(str(arr[-1]) + '\n')
