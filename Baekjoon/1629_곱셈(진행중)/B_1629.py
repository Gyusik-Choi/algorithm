def divide_and_conquer(base, exponent):
    if exponent == 1:
        return base % C

    new_base = divide_and_conquer(base, exponent // 2)

    if exponent % 2 == 1:
        return (new_base * new_base) * base % C
    return new_base * new_base % C


A, B, C = map(int, input().split())
answer = divide_and_conquer(A, B)
print(answer)

# 반례
# 4 1 2
# 정답: 0
