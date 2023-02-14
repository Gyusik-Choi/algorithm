def sliced_word_length(unit, word):
    sliced_word = ''
    temp_word = word[:unit]
    length = 1

    for i in range(unit, len(word), unit):
        w = word[i: i + unit]

        if temp_word == w:
            length += 1
            continue

        sliced_word += str(length) + temp_word if length > 1 else temp_word
        temp_word = w
        length = 1

    sliced_word += str(length) + temp_word if length > 1 else temp_word

    return len(sliced_word)


def solution(s):
    min_length = len(s)

    slice_unit = len(s) // 2

    for unit in range(slice_unit, 0, -1):
        min_length = min(min_length, sliced_word_length(unit, s))

    return min_length


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))

