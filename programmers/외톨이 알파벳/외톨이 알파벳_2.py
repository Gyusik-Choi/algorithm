def solution(input_string):
    arr = []
    for char in input_string:
        if len(arr) and arr[-1] == char:
            continue
        arr.append(char)

    alpha = ''.join(sorted(set(list(filter(lambda x: arr.count(x) > 1, arr)))))
    return alpha if alpha else 'N'


print(solution("edeaaabbccd"))
print(solution("eeddee"))
print(solution("string"))
print(solution("zbzbz"))
