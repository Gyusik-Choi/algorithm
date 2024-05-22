N = int(input())
adventurers = list(map(int, input().split()))
adventurers.sort()

group = 0
cnt = 0

for idx, adventurer in enumerate(adventurers):
    cnt += 1

    if cnt == adventurer:
        group += 1
        cnt = 0

print(group)
