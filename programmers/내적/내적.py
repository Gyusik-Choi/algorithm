def solution(a, b):
    # return sum(list(map(lambda i: a[i] * b[i], range(len(a)))))
    return sum(list(map(lambda x, y: x * y, a, b)))


print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
print(solution([-1, 0, 1], [1, 0, -1]))
