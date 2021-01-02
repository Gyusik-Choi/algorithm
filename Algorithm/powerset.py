def subset(k, n):
    if k == n:
        ans.append(temp[:])
    else:
        temp.append(arr[k])
        subset(k + 1, n)
        temp.pop()
        subset(k + 1, n)


arr = [1, 2, 3]
N = len(arr)
temp = []
ans = []
subset(0, N)
print(ans)