# LIS (최장 증가 부분 수열) 의 갯수를 구하는 방법
# 방법1: 완전탐색
numbers = [10, 20, 30, 10, 30, 40, 20, 50, 60]
lis = [1] * len(numbers)

for i in range(1, len(numbers)):
    for j in range(i - 1, -1, -1):
        if numbers[i] > numbers[j]:
            lis[i] = max(lis[j] + 1, lis[i])

print(lis[-1])
