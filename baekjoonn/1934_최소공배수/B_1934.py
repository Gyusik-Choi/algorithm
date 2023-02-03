def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    gcd = get_gcd(A, B)
    print(A * B // gcd)
