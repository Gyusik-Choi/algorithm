import sys


def multiple(y, x):
    if y % x == 0:
        return True
    return False


def factor(y, x):
    if x % y == 0:
        return True
    return False


while True:
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if not a and not b:
        break

    if a < b:
        if factor(a, b):
            sys.stdout.write("factor" + "\n")
        else:
            sys.stdout.write("neither" + "\n")
    else:
        if multiple(a, b):
            sys.stdout.write("multiple" + "\n")
        else:
            sys.stdout.write("neither" + "\n")
