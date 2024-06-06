def solution(my_string, is_prefix):
    return 1 if my_string[:len(is_prefix)] == is_prefix else 0


print(solution("banana",	"ban"))
print(solution("banana",	"nan"))
print(solution("banana",	"abcd"))
print(solution("banana", "bananan"))
