import sys


N = int(input())

words_dict = {}
for i in range(N):
    word = sys.stdin.readline().rstrip()

    word_len = len(word)
    if word_len in words_dict:
        if word not in words_dict[word_len]:
            words_dict[word_len] += [word]
    else:
        words_dict[word_len] = [word]

words_dict_to_list = sorted(words_dict.items())
for same_len_words in words_dict_to_list:
    sorted_same_len_words = sorted(same_len_words[1])
    for idx, w in enumerate(sorted_same_len_words):
        sys.stdout.write(w + '\n')
