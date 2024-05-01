def solution(cipher, code):
    return ''.join([cipher[i] for i in range(code - 1, len(cipher), code)])


print(solution("dfjardstddetckdaccccdegk", 4))
print(solution("pfqallllabwaoclk", 2))
