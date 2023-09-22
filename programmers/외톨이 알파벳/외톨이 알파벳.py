def get_last_idx(string, target, idx):
    last_idx = idx

    for i in range(idx, len(string)):
        if string[i] != target:
            break

        last_idx = i

    return last_idx


def is_duplicated(input_string, target):
    idx = input_string.index(target)
    last_idx = get_last_idx(input_string, target, idx)

    if last_idx == len(input_string) - 1:
        return False

    if input_string[last_idx + 1:].find(target) == -1:
        return False

    return True


def solution(input_string):
    answer = ''

    for string in set(input_string):
        # a, b, c, d, e
        if is_duplicated(input_string, string):
            answer += string

    if not answer:
        return 'N'

    return ''.join(sorted(answer))


print(solution("edeaaabbccd"))
# print(solution("eeddee"))
# print(solution("string"))
# print(solution("zbzbz"))
