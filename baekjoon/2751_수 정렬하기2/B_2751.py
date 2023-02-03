import sys


def merge_sort(lst):
    if len(lst) < 2:
        return lst
    mid = len(lst) // 2
    low_arr = merge_sort(lst[:mid])
    high_arr = merge_sort(lst[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1

    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


N = int(input())
arr = []
for i in range(N):
    num = int(sys.stdin.readline())
    arr.append(num)
ans = merge_sort(arr)
for n in ans:
    sys.stdout.write(str(n) + '\n')
