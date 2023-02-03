S = list(map(int, input()))

change = 0
start = S[0]
for i in range(1, len(S)):
    if S[i - 1] == start and S[i] != start:
        change += 1
print(change)
