N, B = input().split()
B = int(B)

num = 0
idx = len(N)

for n in N:
    idx -= 1

    if 'A' <= n <= 'Z':
        num += (ord(n) - 55) * (B ** idx)
        continue

    num += int(n) * (B ** idx)

print(num)
