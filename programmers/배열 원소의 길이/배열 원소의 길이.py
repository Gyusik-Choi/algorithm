def solution(str_list):
    return list(map(lambda x: len(x), str_list))


print(solution(["We", "are", "the", "world!"]))
print(solution(["I", "Love", "Programmers."]))
