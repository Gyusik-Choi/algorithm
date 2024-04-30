def solution(my_string):
    return ''.join(filter(lambda x: x not in ["a", "e", "i", "o", "u"], my_string))


print(solution("bus"))
print(solution("nice to meet you"))
