S = list(input())

strings = []
numbers = []

for s in S:
    if 65 <= ord(s) <= 90:
        strings.append(s)
    else:
        numbers.append(s)

strings.sort()
sums = sum(list(map(int, numbers)))

print(''.join(strings) + str(sums))

# K1KA5CB7 => ABCKK13
# 7K1KA5CB => ABCKK13
# AJKDLSI412K4JSJ9D => ADDIJJJKKLSS20
