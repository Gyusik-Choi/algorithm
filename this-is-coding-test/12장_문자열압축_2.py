def solution(s):
    half = len(s) // 2
    slice_length = half

    min_length = len(s)
    while slice_length > 0:
        same_cnt = 1
        characters = ''
        prior_char = s[:slice_length]

        for i in range(slice_length, len(s), slice_length):
            current_char = s[i: i + slice_length]
            if slice_length == 3:
                print(current_char)
            if prior_char == current_char:
                same_cnt += 1
            else:
                if same_cnt > 1:
                    characters += str(same_cnt) + prior_char
                else:
                    characters += prior_char
                same_cnt = 1

            prior_char = current_char

        if same_cnt > 1:
            characters += str(same_cnt) + prior_char
        else:
            characters += prior_char

        min_length = min(min_length, len(characters))
        slice_length -= 1

    return min_length


# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))
