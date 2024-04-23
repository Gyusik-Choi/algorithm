def solution(my_string):
    return sum(map(int, filter(lambda x: x.isdecimal(), my_string)))


print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))
