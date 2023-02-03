import sys


N = int(sys.stdin.readline().rstrip())
numbers = []
for _ in range(N):
    number = int(sys.stdin.readline().rstrip())
    numbers.append(number)

stack = []
answer = []
ascending_num = 0
flag = True
for number in numbers:
    while ascending_num + 1 <= number:
        stack.append(ascending_num + 1)
        answer.append("+")
        ascending_num += 1

    if number == stack[-1]:
        stack.pop()
        answer.append("-")
    else:
        flag = False
        break

if not flag:
    sys.stdout.write("NO" + "\n")
else:
    for a in answer:
        sys.stdout.write(a + "\n")
