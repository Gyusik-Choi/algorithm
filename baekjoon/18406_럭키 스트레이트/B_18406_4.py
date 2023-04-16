N = list(map(int, input()))
half_idx = len(N) // 2
left_half = sum(N[:half_idx])
right_half = sum(N[half_idx:])
# print('LUCKY' if left_half == right_half else 'READY')
# 백준 채점시 위의 코드는 런타임 에러 (ValueError) 발생
print('LUCKY') if left_half == right_half else print('READY')