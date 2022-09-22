import sys


N = int(sys.stdin.readline())
max_length = N * 2 - 1
start = max_length // 2

# start 에서 출발하여
# start 지점을 1 씩 감소하면서
# 별을 찍는 횟수는 2씩 증가

length = 1
for n in range(N):
    for i in range(start + 1):
        if i == start:
            for j in range(length):
                sys.stdout.write('*')
        else:
            sys.stdout.write(' ')

    start -= 1
    length += 2
    sys.stdout.write('\n')
