def solution(s):
    words = s.split(' ')

    for idx, word in enumerate(words):
        if not word:
            continue

        word_list = list(word)
        words[idx] = word_list[0].upper() + ''.join(word_list[1:]).lower()

    return ' '.join(words)


print(solution("3people unFollowed me"))
print(solution("for the last week"))
print(solution("3people  unFollowed me"))
