N = int(input())
adventurers = list(map(int, input().split()))
adventurers.sort()

answer = 0
cnt = 0

for a in adventurers:
    cnt += 1

    if cnt != a:
        continue

    answer += 1
    cnt = 0

print(answer)
