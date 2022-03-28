S = list(map(int, input()))

max_num = 0
for s in S:
    if max_num == 0 or s == 0 or s == 1:
        max_num += s
    else:
        max_num *= s

print(max_num)
