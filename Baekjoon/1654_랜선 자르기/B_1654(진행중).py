import sys


def binary_search(start, end, target):
    if start > end:
        return

    mid = (start + end) // 2
    
    sums = 0
    for j in range(K):
        candidate = lan_lines[j]
        sums += candidate // mid

    if sums >= target:
        answer_candidates.append(mid)
        binary_search(mid + 1, end, target)
    else:
        binary_search(start, mid - 1, target)


K, N = map(int, sys.stdin.readline().split())
lan_lines = []
for i in range(K):
    lan = int(sys.stdin.readline().rstrip())
    lan_lines.append(lan)

if K == N:
    sys.stdout.write(str(min(lan_lines)))
else:
    answer_candidates = []
    binary_search(1, max(lan_lines), N)
    sys.stdout.write(str(max(answer_candidates)))

# 457, 539, 743, 802
# K 개의 랜선 각각으로 모두 만들 수 있는 공통적인 최대 길이의 랜선
# => 아니다. 공통으로 만족하지 않아도 된다. 최대 길이로 N 갯수만 맞출 수 있으면 된다

# 200
# 2
# 2
# 3
# 4

# 이분 탐색 문제라 선형으로 하나식 찾지 말라는 문제인데...

# 200 300 400 500
# 12

# 100
# 2
# 3
# 4
# 5

# 150
# 1
# 2
# 2
# 3

# 125
# 1
# 2
# 3
# 4

# 112
# 1
# 2
# 3
# 4

# (1, 200)
# 100
# (101, 200)
# 150
# (101, 149)
# 125
# (101, 124)
# 112

# 반례
# https://joey09.tistory.com/115

# 추가 반례
# 3 5
# 5
# 5
# 4
# 정답 2

