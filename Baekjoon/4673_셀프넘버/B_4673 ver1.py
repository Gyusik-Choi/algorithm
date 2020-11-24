N = 10000
arr = [1] * (N + 1)
for num in range(1, N + 1):
    if arr[num]:
        total = num
        while True:
            sums = 0
            str_num = str(total)
            for j in range(len(str_num)):
                sums += int(str_num[j])
            total += sums
            if total <= 10000:
                arr[total] = 0
            else:
                break
for i in range(1, len(arr)):
    if arr[i]:
        print(i)
