T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr1 = set(list(input().split()))
    arr2 = set(list(input().split()))
    print("#{} {}".format(t, len(arr1 & arr2)))
