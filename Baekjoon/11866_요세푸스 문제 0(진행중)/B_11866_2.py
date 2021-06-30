import sys


N, K = map(int, sys.stdin.readline().split())
numbers = [i for i in range(1, N + 1)]
answer = "<"

while len(numbers) > 0:
    cnt = K - 1
    while cnt > 0:
        pop_number = numbers.pop(0)
        numbers.append(pop_number)
        cnt -= 1
    answer += str(numbers.pop(0)) + ", "
answer = answer.rstrip(", ")
answer += ">"
sys.stdout.write(answer)

# 참고
# https://st-lab.tistory.com/197
