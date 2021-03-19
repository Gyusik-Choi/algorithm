N = int(input())
arr = list(map(int, input().split()))
time_table = sorted(arr)

prior_sums = 0
sums = 0
for time in time_table:
    prior_sums += time
    sums += prior_sums
print(sums)
