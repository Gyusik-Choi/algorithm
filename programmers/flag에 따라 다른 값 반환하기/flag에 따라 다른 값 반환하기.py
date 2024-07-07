def solution(a, b, flag):
    return a + b if flag else a - b


print(solution(-4, 7, True))
print(solution(-4, 7, False))
