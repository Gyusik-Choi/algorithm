N = int(input())
people = [input().split() for _ in range(N)]
rainbow_dance_people = {'ChongChong': True}

for i, p in enumerate(people):
    a, b = p

    if a in rainbow_dance_people or b in rainbow_dance_people:
        rainbow_dance_people[a] = True
        rainbow_dance_people[b] = True

print(len(rainbow_dance_people))
