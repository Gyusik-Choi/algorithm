N = int(input())
arr = list(map(int, input().split()))
time_table = sorted(arr)

sums = 0
for i in range(len(time_table) - 1, -1, -1):
    for j in range(i + 1):
        sums += time_table[j]

print(sums)
