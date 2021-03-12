import math


def permutation(idx):
    if idx == N - 1:
        operator_perm.append(perm[:])
        return
    else:
        for k in range(N - 1):
            if not check[k]:
                check[k] = 1
                perm.append(operators[k])
                permutation(idx + 1)
                check[k] = 0
                perm.pop()


N = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))

operators = []
for i in range(len(operator)):
    if operator[i] != 0:
        for j in range(operator[i]):
            if i == 0:
                operators.append("+")
            elif i == 1:
                operators.append("-")
            elif i == 2:
                operators.append("*")
            else:
                operators.append("//")

perm = []
# 연산자 순열
operator_perm = []
check = [0] * (N - 1)
# 순열 함수
permutation(0)

# 연산자 순열에서 하나씩 꺼내서 값 계산
max_sums = -float('inf')
min_sums = float('inf')

for operate in operator_perm:
    sums = nums[0]
    for o in range(len(operate)):
        if operate[o] == "+":
            sums += nums[o + 1]
        elif operate[o] == "-":
            sums -= nums[o + 1]
        elif operate[o] == "*":
            sums *= nums[o + 1]
        else:
            if sums < 0:
                division = math.ceil(sums / nums[o + 1])
                sums = division
            else:
                sums //= nums[o + 1]
    if max_sums < sums:
        max_sums = sums
    if min_sums > sums:
        min_sums = sums

print(max_sums)
print(min_sums)
