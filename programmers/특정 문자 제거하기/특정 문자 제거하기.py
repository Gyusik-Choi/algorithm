def solution(my_string, letter):
    return ''.join([char for char in my_string if char != letter])


print(solution("abcdef", "f"))
print(solution("BCBdbe", "B"))
