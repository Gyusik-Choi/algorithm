def rabin_karp(w, p):
    word_length = len(w)
    pattern_length = len(p)

    word_hash = 0
    pattern_hash = 0
    power = 1

    for i in range(0, word_length - pattern_length + 1):
        if not i:
            for j in range(0, pattern_length):
                word_hash += word[word_length] * power


word = "ababacabacaabacaaba"
pattern = "abacaaba"

rabin_karp(word, pattern)

# 참고
# https://m.blog.naver.com/ndb796/221240679247
# 해시 알고리즘을 활용한 문자 탐색 알고리즘
# 해시에 대해서 함께 이해할 수 있는 알고리즘
