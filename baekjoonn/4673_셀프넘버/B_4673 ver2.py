N = 10000
arr = [1] * (N + 1)
for num in range(1, N + 1):
    if arr[num]:
        total = num
        while True:
            sums = total
            while total != 0:
                sums += total % 10
                total = total // 10
            if sums <= 10000:
                arr[sums] = 0
                total = sums
            else:
                break
for i in range(1, len(arr)):
    if arr[i]:
        print(i)
