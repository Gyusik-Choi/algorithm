def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()


print(solution("a234"))
print(solution("1234"))
