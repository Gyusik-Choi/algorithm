import sys


K = int(input())
stack = []
for i in range(K):
    number = int(sys.stdin.readline().strip())
    if number != 0:
        stack.append(number)
    else:
        stack.pop()

if stack:
    sys.stdout.write(str(sum(stack)))
else:
    sys.stdout.write(str(0))
