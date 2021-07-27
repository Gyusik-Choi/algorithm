import sys


N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))

stack = []
for i in range(N):
    while stack:
        if numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            numbers[idx] = numbers[i]
        else:
            break
    stack.append(i)

while stack:
    idx = stack.pop()
    numbers[idx] = -1

answer = ""
for number in numbers:
    answer += str(number) + " "
answer.rstrip(" ")
sys.stdout.write(answer)
