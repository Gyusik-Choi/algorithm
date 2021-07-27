import sys


N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))

stack = []
for i in range(N):
    if not stack:
        stack.append(i)
    else:
        if numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            numbers[idx] = numbers[i]
            if stack:
                for j in range(len(stack) - 1, -1, -1):
                    if numbers[stack[j]] < numbers[i]:
                        idx = stack.pop()
                        numbers[idx] = numbers[i]
                    else:
                        break
            stack.append(i)
        else:
            stack.append(i)

while stack:
    idx = stack.pop()
    numbers[idx] = -1

for number in numbers:
    sys.stdout.write(str(number) + " ")
