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
        return binary_search(mid + 1, end, target)
    else:
        return binary_search(start, mid - 1, target)


K, N = map(int, sys.stdin.readline().split())
lan_lines = []
for i in range(K):
    lan = int(sys.stdin.readline().rstrip())
    lan_lines.append(lan)

# if K == N:
#     sys.stdout.write(str(min(lan_lines)))
# else:
answer_candidates = []
binary_search(1, max(lan_lines), N)
sys.stdout.write(str(max(answer_candidates)))

# K 개의 랜선 각각으로 모두 만들 수 있는 공통적인 최대 길이의 랜선
# => 아니다. 공통으로 만족하지 않아도 된다. 최대 길이로 N 갯수만 맞출 수 있으면 된다

# 반례
# https://joey09.tistory.com/115

# 추가 반례
# 3 5
# 5
# 5
# 4
# 정답: 2

# 추가 반례
# 11 46
# 2147483635
# 2147483595
# 2147483585
# 2147483641
# 2147483552
# 2147483637
# 2147483570
# 2147483563
# 2147483621
# 2147483618
# 2147483553
# 정답: 429496727
