def rabin_karp(w, p):
    word_length = len(w)
    pattern_length = len(p)

    word_hash = 0
    pattern_hash = 0
    power = 1

    for i in range(0, word_length - pattern_length + 1):
        if i == 0:
            for j in range(pattern_length):
                word_hash += ord(word[pattern_length - 1 - j]) * power
                pattern_hash += ord(pattern[pattern_length - 1 - j]) * power

                if j < pattern_length - 1:
                    power *= 2
        else:
            word_hash = 2 * (word_hash - ord(word[i - 1]) * power) + ord(word[i + pattern_length - 1])

        if word_hash == pattern_hash:
            flag = True
            for k in range(pattern_length):
                if word[k + i] != pattern[k]:
                    flag = False
                    break

            if flag:
                print("{}번째에서 찾았습니다".format(i + 1))


word = "ababacabacaabacaaba"
pattern = "abacaaba"

rabin_karp(word, pattern)

# 참고
# https://m.blog.naver.com/ndb796/221240679247
# https://m.blog.naver.com/kks227/220927272165
# https://junstar92.tistory.com/125
# 해시 알고리즘을 활용한 문자 탐색 알고리즘
# 해시에 대해서도 함께 이해할 수 있는 알고리즘
