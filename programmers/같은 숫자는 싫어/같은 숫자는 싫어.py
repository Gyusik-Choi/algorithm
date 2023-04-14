def solution(arr):
    q = []

    for i, a in enumerate(arr):
        if q and q[-1] == a:
            continue

        q.append(a)

    return q


print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))
