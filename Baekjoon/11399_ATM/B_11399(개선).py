N = int(input())
arr = list(map(int, input().split()))
time_table = sorted(arr)

sums = 0
n = N
for time in time_table:
    sums += time * n
    n -= 1
print(sums)
