def solution(a, b):
    a = sorted(a)
    b = sorted(b, reverse=True)
    return sum(map(lambda arg: a[arg[0]] * b[arg[0]], enumerate(range(len(a)))))


print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))
