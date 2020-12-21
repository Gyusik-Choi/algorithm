def selection_sort(lst):
    for j in range(len(lst) - 1):
        min_idx = j
        for k in range(j + 1, len(lst)):
            if lst[min_idx] > lst[k]:
                min_idx = k
        lst[j], lst[min_idx] = lst[min_idx], lst[j]
    return lst


N = int(input())
arr = []
for i in range(N):
    num = int(input())
    arr.append(num)

ans = selection_sort(arr)
for n in ans:
    print(n)
