def solution(d, budget):
    cnt = 0

    for money in sorted(d):
        if budget - money < 0:
            break
        cnt += 1
        budget -= money

    return cnt


print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))
