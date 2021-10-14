import sys


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    F = int(sys.stdin.readline().rstrip())
    friends = {}
    for _ in range(F):
        name1, name2 = sys.stdin.readline().split()

        # dictionary
        # pass_compression
