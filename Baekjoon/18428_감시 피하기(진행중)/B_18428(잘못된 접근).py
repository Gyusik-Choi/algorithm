import copy


def dfs_recursion(start):
    pass


def combinations(idx, num, limit):
    if idx == limit:
        combs.append(temp_comb[:])
    else:
        for n in range(num, len(empty)):
            temp_comb.append(n)
            combinations(idx + 1, n + 1, limit)
            temp_comb.pop()


N = int(input())
corridor = [list(input().split()) for _ in range(N)]

empty = []
teachers = []
for i, row in enumerate(corridor):
    for j, item in enumerate(row):
        if item == 'X':
            empty.append([i, j])
        elif item == 'T':
            teachers.append([i, j])

combs = []
temp_comb = []
combinations(0, 0, 3)

y_direction = [-1, 0, 1, 0]
x_direction = [0, 1, 0, -1]

for i, comb in enumerate(combs):
    for j, c in enumerate(comb):
        y = empty[c][0]
        x = empty[c][1]

        corridor[y][x] = 'O'

    copied_corridor = copy.deepcopy(corridor)

    for teacher in teachers:
        dfs_recursion(teacher)

    for j, c in enumerate(comb):
        y = empty[c][0]
        x = empty[c][1]

        corridor[y][x] = 'X'
