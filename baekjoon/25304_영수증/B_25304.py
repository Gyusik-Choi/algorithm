import sys


X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
sums = 0
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    sums += a * b

sys.stdout.write('Yes' if X == sums else 'No')
