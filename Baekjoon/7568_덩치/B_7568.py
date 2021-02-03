N = int(input())
people = []
for i in range(N):
    height, weight = map(int, input().split())
    people.append([height, weight])

idx = 0
ans = [0] * N
while idx < len(people):
    cnt = 0
    for j in range(len(people)):
        if j != idx:
            if people[idx][0] < people[j][0] and people[idx][1] < people[j][1]:
                cnt += 1
    ans[idx] = str(cnt + 1)
    idx += 1
print(' '.join(ans))