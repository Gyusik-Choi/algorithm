N = int(input())
adventurers = list(map(int, input().split()))
adventurers.sort()

total_groups = 0
members = 0
for adventurer in adventurers:
    members += 1
    if adventurer == members:
        total_groups += 1
        members = 0

print(total_groups)
