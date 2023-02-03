import sys


N = int(input())

words = []
for i in range(N):
    word = sys.stdin.readline().rstrip()
    word_len = len(word)
    words.append([word_len, word])

sorted_words = sorted(words, key=lambda x: (x[0], x[1]))
print(sorted_words[0][1])
for i in range(1, len(sorted_words)):
    if sorted_words[i][1] != sorted_words[i - 1][1]:
        sys.stdout.write(sorted_words[i][1] + '\n')
