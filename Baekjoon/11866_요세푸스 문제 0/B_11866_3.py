import sys


N, K = map(int, sys.stdin.readline().split())
numbers = [i for i in range(1, N + 1)]

answer = "<"
idx = 0
while len(numbers) > 0:
    length = len(numbers)
    idx = (idx + K - 1) % length
    pop_number = numbers.pop(idx)
    answer += str(pop_number) + ", "

answer = answer.rstrip(", ")
answer += ">"
sys.stdout.write(answer)

# 참고
# https://st-lab.tistory.com/197
