import math


N, K = map(int, input().split())
square_root = int(math.sqrt(N))
divisor = []

for root in range(1, square_root + 1):
    quotient, remainder = divmod(N, root)

    if not remainder:
        if root == quotient:
            divisor.append(root)
            continue

        divisor.append(root)
        divisor.append(quotient)

if len(divisor) < K:
    print(0)
else:
    divisor.sort()
    print(divisor[K - 1])
