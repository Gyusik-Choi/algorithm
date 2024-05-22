def get_combinations(idx, limit):
    global combinations

    if idx == limit:
        combinations.append(sum(temp_combination))
    else:
        for j in range(N):
            if not visited[j]:
                visited[j] = True
                temp_combination.append(coins[j])
                get_combinations(idx + 1, limit)
                visited[j] = False
                temp_combination.pop()


N = int(input())
coins = list(map(int, input().split()))

min_coin = 1
combinations = []
for i in range(N):
    temp_combination = []
    visited = [False] * N
    get_combinations(0, i)

combinations.sort()
answer = 1
for i in range(1, combinations[-1]):
    if i not in combinations:
        answer = i
        break

print(answer)

# 5
# 3 2 2 1 9
# => 8