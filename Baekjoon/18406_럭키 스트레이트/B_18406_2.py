N = list(map(int, input()))
half = len(N) // 2

left = N[:half]
right = N[half:]

sum_left = sum(left)
sum_right = sum(right)

if sum_left == sum_right:
    print('LUCKY')
else:
    print('READY')
