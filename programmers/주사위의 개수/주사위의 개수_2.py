def solution(box, n):
    cnt = 1
    for b in box:
        cnt *= (b // n)
    return cnt


print(solution([1, 1, 1,], 1))
print(solution([10, 8, 6], 3))
