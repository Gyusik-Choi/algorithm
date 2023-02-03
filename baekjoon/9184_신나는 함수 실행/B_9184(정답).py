import sys


def start(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        memo[(x, y, z)] = 1
        return memo[(x, y, z)]
    else:
        if (x, y, z) in memo:
            return memo[(x, y, z)]
        else:
            if x > 20 or y > 20 or z > 20:
                memo[(x, y, z)] = start(20, 20, 20)
                return memo[(x, y, z)]
            elif x < y < z:
                memo[(x, y, z)] = start(x, y, z - 1) + start(x, y - 1, z - 1) - start(x, y - 1, z)
                return memo[(x, y, z)]
            else:
                memo[(x, y, z)] = start(x - 1, y, z) + start(x - 1, y - 1, z) + start(x - 1, y, z - 1) - start(x - 1, y - 1, z - 1)
                return memo[(x, y, z)]


memo = {}
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        ans = start(a, b, c)
        print("w({}, {}, {}) = {}".format(a, b, c, ans))