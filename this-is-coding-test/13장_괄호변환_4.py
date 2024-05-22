def change_direction(word):
    new_word = ''

    for w in word:
        if w == '(':
            new_word += ')'
        else:
            new_word += '('

    return new_word


def is_correct_word(word):
    stack = []

    for w in word:
        if w == '(':
            stack.append(w)
            continue

        if not stack:
            return False

        stack.pop()

    if stack:
        return False

    return True


def split_word(word):
    left_cnt = 0
    right_cnt = 0

    for i in range(len(word)):
        if word[i] == '(':
            left_cnt += 1
        else:
            right_cnt += 1

        if left_cnt == right_cnt:
            break

    return [word[:left_cnt + right_cnt], word[left_cnt + right_cnt:]]


def solution(word):
    if not word:
        return ''

    u, v = split_word(word)

    if is_correct_word(u):
        return u + solution(v)

    empty_word = '('

    empty_word += solution(v)

    empty_word += ')'

    empty_word += change_direction(u[1:-1])

    return empty_word


# print(solution("(()())()"))
# print(solution(")("))
# print(solution("()))((()"))
