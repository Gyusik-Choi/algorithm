def solution(rsp):
    return ''.join(["0" if char == "2" else "5" if char == "0" else "2" for char in rsp])


print(solution("2"))
print(solution("205"))
