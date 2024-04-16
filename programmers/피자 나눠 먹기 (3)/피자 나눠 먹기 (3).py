def solution(slices, n):
    return (n + (slices - 1)) // slices


print(solution(7, 10))
print(solution(4, 12))

# slice 4
# 1판 -> n: 1 ~ 4
# 2판 -> n: 5 ~ 8
# 3판 -> n: 9 ~ 12
