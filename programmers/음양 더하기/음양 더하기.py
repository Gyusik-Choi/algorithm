def solution(absolutes, signs):
    answer = 0

    for idx, sign in enumerate(signs):
        if sign:
            answer += absolutes[idx]
        else:
            answer -= absolutes[idx]

    return answer
