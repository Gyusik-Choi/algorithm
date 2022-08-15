S = list(map(int, input()))
cnt = [0, 0]

cnt[S[0]] += 1
for i in range(1, len(S)):
    if S[i - 1] != S[i]:
        cnt[S[i]] += 1

print(min(cnt))
