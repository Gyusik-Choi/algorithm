# 데이터 갯수 n과 데이터 입력 받기
n = 5
data = [10, 20, 30, 40, 50]

# Prefix Sum 배열 계산
summary = 0
prefix_sum = [0]
for i in data:
    summary += i
    prefix_sum.append(summary)

# 구간합 계산
left = 3
right = 4
print(prefix_sum)
print(prefix_sum[right] - prefix_sum[left - 1])

# 참고
# https://www.youtube.com/watch?v=rI8NRQsAS_s
