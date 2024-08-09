def solution(str_arr):
    return [str_arr[i].lower() if not i % 2 else str_arr[i].upper() for i in range(len(str_arr))]


print(solution(["AAA", "BBB", "CCC", "DDD"]))
