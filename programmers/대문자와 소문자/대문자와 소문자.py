def solution(my_string):
    return ''.join([x.upper() if x.islower() else x.lower() for x in my_string])


print(solution("cccCCC"))
print(solution("abCdEfghIJ"))
