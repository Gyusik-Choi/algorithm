import sys


N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))
numbers = sorted(numbers)
numbers_to_dict = dict()
for number in numbers:
    if number in numbers_to_dict.keys():
        numbers_to_dict[number] += 1
    else:
        numbers_to_dict[number] = 1

M = int(sys.stdin.readline().rstrip())
number_to_find = list(map(int, sys.stdin.readline().split()))

answer = []
for num in number_to_find:
    if num in numbers_to_dict.keys():
        answer.append(str(numbers_to_dict[num]))
    else:
        answer.append(str(0))

print(' '.join(answer))
