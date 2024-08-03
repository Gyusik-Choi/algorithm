import re


def solution(rny_string):
    return re.sub('m', 'rn', rny_string)


print(solution("masterpiece"))
print(solution("programmers"))
