import sys


N = int(input())

words = []
for i in range(N):
    word = sys.stdin.readline().rstrip()
    words.append(word)

words.sort()
sorted_words = sorted(words, key=len)
sys.stdout.write(sorted_words[0] + '\n')
for i in range(1, len(sorted_words)):
    if sorted_words[i] != sorted_words[i - 1]:
        sys.stdout.write(sorted_words[i] + '\n')
