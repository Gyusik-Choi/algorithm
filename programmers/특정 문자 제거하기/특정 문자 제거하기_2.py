def solution(my_string, letter):
    return ''.join(filter(lambda char: char != letter, my_string))


print(solution("abcdef", "f"))
print(solution("BCBdbe", "B"))
