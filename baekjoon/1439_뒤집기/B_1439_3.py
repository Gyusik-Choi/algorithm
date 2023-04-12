S = list(map(int, input()))
prev = -1
cnt_zero = 0
cnt_one = 0
for i, s in enumerate(S):
    if prev == s:
        continue

    if s == 0:
        cnt_zero += 1
    else:
        cnt_one += 1

    prev = s

print(min(cnt_zero, cnt_one))
