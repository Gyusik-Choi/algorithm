def solution(my_string, is_suffix):
    # return 1 if my_string[::-1][:len(is_suffix)] == is_suffix[::-1] else 0
    return 1 if my_string[::-1][:len(is_suffix)] == is_suffix else 0


print(solution("abcde", "de"))
# abcde
# de
