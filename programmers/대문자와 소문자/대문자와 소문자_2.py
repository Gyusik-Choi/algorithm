def solution(my_string):
    return ''.join(map(lambda x: x.upper() if x.islower() else x.lower(), my_string))


print(solution("cccCCC"))
print(solution("abCdEfghIJ"))

