def solution(my_string):
    return [s for s in my_string.strip(" ").split(" ") if s]


print(solution(" i    love  you"))
print(solution("    programmers  "))
