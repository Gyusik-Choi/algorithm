import sys


N = int(sys.stdin.readline())
houses = list(map(int, sys.stdin.readline().split()))
houses.sort()

half = 0
if not N % 2:
    half = N // 2 - 1
else:
    half = N // 2

print(houses[half])
