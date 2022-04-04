def get_sums(arr, start_idx, last_idx):
    sums = 0
    for i in range(start_idx, last_idx):
        sums += arr[i]

    return sums


N = list(map(int, input()))
length = len(N)
half = length // 2

left_sums = get_sums(N, 0, half)
right_sums = get_sums(N, half, length)

if left_sums == right_sums:
    print('LUCKY')
else:
    print('READY')

# 이것이 코딩테스트다 수록 문제
