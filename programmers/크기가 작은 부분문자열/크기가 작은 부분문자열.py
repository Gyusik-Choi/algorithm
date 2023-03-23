def solution(t, p):
    answer = 0

    t_length = len(t)
    p_length = len(p)

    num_p = int(p)

    for i in range(t_length - p_length + 1):
        num_t = int(t[i: i + p_length])

        if num_t <= num_p:
            answer += 1

    return answer


print(solution("3141592", "271"))
print(solution("500220839878", "7"))
print(solution("10203", "15"))
print(solution("102", "102"))