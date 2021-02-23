import sys


def start(x, y, z):
    str_x = str(x)
    str_y = str(y)
    str_z = str(z)
    str_xyz = str_x + str_y + str_z

    if x <= 0 or y <= 0 or z <= 0:
        memo[str_xyz] = 1
        return memo[str_xyz]
    else:
        if str_xyz in memo:
            return memo[str_xyz]
        else:
            if x > 20 or y > 20 or z > 20:
                memo[str_xyz] = start(20, 20, 20)
                return memo[str_xyz]
            elif x < y < z:
                memo[str_xyz] = start(x, y, z - 1) + start(x, y - 1, z - 1) - start(x, y - 1, z)
                return memo[str_xyz]
            else:
                memo[str_xyz] = start(x - 1, y, z) + start(x - 1, y - 1, z) + start(x - 1, y, z - 1) - start(x - 1, y - 1, z - 1)
                return memo[str_xyz]


memo = {}
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        ans = start(a, b, c)
        print("w({}, {}, {}) = {}".format(a, b, c, ans))
