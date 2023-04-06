import sys


N = 5
M = 15
words = [[''] * M for _ in range(N)]

for i in range(N):
    word = list(sys.stdin.readline())
    word.pop()

    for j in range(len(word)):
        words[i][j] = word[j]

for j in range(M):
    for i in range(N):
        if words[i][j]:
            sys.stdout.write(words[i][j])
