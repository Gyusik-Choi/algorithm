def solution(cipher, code):
    plain = ""
    for i in range(code - 1, len(cipher), code):
        plain += cipher[i]
    return plain


print(solution("dfjardstddetckdaccccdegk", 4))
print(solution("pfqallllabwaoclk", 2))
