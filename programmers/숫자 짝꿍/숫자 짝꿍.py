def solution(x: str, y: str):
    same_nums_dict = dict()

    for char_x in x:
        if char_x not in same_nums_dict:
            same_nums_dict[char_x] = [1, 0]
        else:
            same_nums_dict[char_x][0] += 1

    for char_y in y:
        if char_y in same_nums_dict:
            same_nums_dict[char_y][1] += 1

    same_nums = []

    for key, value in same_nums_dict.items():
        if not value[0] or not value[1]:
            continue

        for _ in range(min(value)):
            same_nums.append(key)

    if not len(same_nums):
        return "-1"

    if set(same_nums) == {"0"}:
        return "0"

    return ''.join(sorted(same_nums, reverse=True))


print(solution("100", "2345"))
print(solution("100", "203045"))
print(solution("100", "123450"))
print(solution("12321", "42531"))
print(solution("5525", "1255"))
