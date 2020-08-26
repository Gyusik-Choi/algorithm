def convert(num, base):
    t = "0123456789ABCDEF"
    quotient, remainder = divmod(num, base)
    if quotient == 0:
        return t[remainder]
    else:
        return convert(quotient, base) + t[remainder]


def solution(n, t, m, p):
    answer = ''
    len_answer = 0
    limit = t * m
    num = 0
    while len_answer < limit:
        converted_num = convert(num, n)
        answer += converted_num
        len_answer += len(converted_num)
        num += 1
    return answer[p-1:len(answer):m][:t]


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))
