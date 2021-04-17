import sys


def binary_search(start, end, n):
    # 만약에 시작 인덱스가 끝 인덱스 보다 크다면 대상 숫자 n이 배열 내에 없다는 의미
    if start > end:
        return 0

    # 중앙 인덱스
    mid = (start + end) // 2

    # 만약에 대상 숫자 n이 중앙 값이라면 찾은 것
    if arr1[mid] == n:
        return 1
    # n이 중앙 값보다 작다면 중앙 값보다 왼쪽에 위치한다
    elif arr1[mid] > n:
        return binary_search(start, mid - 1, n)
    # n이 중앙 값보다 크다면 중앙 값보다 오른쪽에 위치한다
    else:
        return binary_search(mid + 1, end, n)


N = int(input())
arr1 = list(map(int, input().split()))
arr1 = sorted(arr1)

M = int(input())
arr2 = list(map(int, input().split()))

for num in arr2:
    ans = binary_search(0, N - 1, num)
    sys.stdout.write(str(ans) + "\n")
