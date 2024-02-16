S = input()
words = set()

for length in range(1, len(S) + 1):
    for idx in range(len(S) - length + 1):
        words.add(S[idx: idx + length])

print(len(words))
