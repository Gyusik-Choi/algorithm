def solution(k, m, score):
    score.sort(reverse=True)

    profit = 0

    for i in range(0, len(score), m):
        if i + m > len(score):
            break

        one_box = score[i: i + m]
        profit += one_box[-1] * m

    return profit


print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))

# 상자에 사과 갯수는 딱 맞춰서 들어가야 한다
# 상자에 사과를 못 채우면 그 상자는 버린다
