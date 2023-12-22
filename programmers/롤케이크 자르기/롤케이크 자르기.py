def solution(topping):
    answer = 0
    older_brother = dict()
    younger_brother = dict()

    for top in topping:
        if top in younger_brother:
            younger_brother[top] += 1
        else:
            younger_brother[top] = 1

    for top in topping:
        if top in older_brother:
            older_brother[top] += 1
        else:
            older_brother[top] = 1

        younger_brother[top] -= 1

        if not younger_brother[top]:
            del younger_brother[top]

        if len(older_brother) == len(younger_brother):
            answer += 1

    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
