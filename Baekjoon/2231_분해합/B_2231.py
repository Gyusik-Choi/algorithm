N = int(input())
min_num = N
cnt = 0
for i in range(N, 0, -1):
    num = i
    decomposition = i
    while i != 0:
        a = i % 10
        i = i // 10
        decomposition += a
    if decomposition == N:
        cnt += 1
        if min_num > num:
            min_num = num
if cnt == 0:
    print(0)
else:
    print(min_num)



