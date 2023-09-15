def dfs(limit, words, arr, target):
    answer = 0
    cnt = 0

    def recursion(max_length, characters, lst, character):
        nonlocal answer, cnt

        if ''.join(lst) == target:
            answer = cnt
            return

        if len(lst) == max_length:
            return

        for i in range(max_length):
            cnt += 1

            lst.append(characters[i])
            recursion(max_length, characters, lst, character)
            lst.pop()

    recursion(limit, words, arr, target)
    return answer


def solution(word):
    return dfs(5, ["A", "E", "I", "O", "U"], [], word)


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))
