def solution(my_string):
    r_string = ''
    for s in my_string:
        r_string = s + r_string
    return r_string


print(solution("jaron"))
