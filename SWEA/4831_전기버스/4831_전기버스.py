# import sys
# sys.stdin = open("input.txt", "r")


def charge(lst, k, n):
    i = 0
    cnt = 0
    while i + k < n:
        for j in range(i + k, i, -1):
            if j in lst or j >= n:
                i = j
                cnt += 1
                break
        else:
            return 0
    return cnt


T = int(input())
for t in range(1, T+1):
    # K 최대 이동 거리, N 정류장, M 충전기 설치된 정류장
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print("#{} {}".format(t, charge(arr, K, N)))
