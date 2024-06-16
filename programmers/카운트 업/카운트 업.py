def solution(my_string, is_suffix):
    return 1 if my_string[::-1][:len(is_suffix)] == is_suffix else 0


print(solution("banana", "a"))
print(solution("banana", "an"))
print(solution("banana", "ana"))
print(solution("banana", "anan"))
print(solution("banana", "anana"))
print(solution("banana", "ananab"))
print(solution("banana", "banana"))
print(solution("bbb", "bbb"))
