import sys


n, m = map(int, sys.stdin.readline().split())

first_player = []
second_player = []
for i in range(m):
    num1, num2 = map(int, sys.stdin.readline().split())
    if i % 2 == 0:
        first_player.append([num1, num2])
    else:
        second_player.append([num1, num2])

# disjoint-set
