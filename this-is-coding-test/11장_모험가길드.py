N = int(input())
adventurers = list(map(int, input().split()))
adventurers.sort()

number_of_groups = 0
group = 0
for a in adventurers:
    group += 1
    if group >= a:
        number_of_groups += 1
        group = 0

print(number_of_groups)

# 5
# 2 3 1 2 2
# => 2

# 9
# 1 2 3 3 3 4 4 5 6
# => 2

# 9
# 1 1 2 2 3 4 5 5 6
# => 3
