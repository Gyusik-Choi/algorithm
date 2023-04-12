S = input()
sums = 0
for s in S:
    s = int(s)
    if sums < 2 or s < 2:
        sums += s
    else:
        sums *= s
print(sums)
