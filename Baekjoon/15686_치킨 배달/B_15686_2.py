def combination(limit, cnt, temp_combination):
    if limit == cnt:
        combinations.append(temp_combination[:])
        return

    for k in range(len(chicken_store)):
        if not temp_combination:
            temp_combination.append(k)
            chosen[k] = True
            combination(limit, cnt + 1, temp_combination)
            temp_combination.pop()
            chosen[k] = False
        else:
            if not chosen[k] and temp_combination[-1] < k:
                temp_combination.append(k)
                chosen[k] = True
                combination(limit, cnt + 1, temp_combination)
                temp_combination.pop()
                chosen[k] = False


N, M = map(int, input().split())
city_info = []
for _ in range(N):
    city = list(map(int, input().split()))
    city_info.append(city)

house = []
chicken_store = []

for i, city in enumerate(city_info):
    for j, c in enumerate(city):
        if c == 1:
            house.append([i, j])
        elif c == 2:
            chicken_store.append([i, j])

combinations = []
chosen = [False] * len(chicken_store)
combination(M, 0, [])

min_distance = float('inf')
for comb in combinations:
    min_house = [float('inf')] * len(house)

    for idx_c, c in enumerate(comb):
        c_y, c_x = chicken_store[c]

        for idx_h, h in enumerate(house):
            h_y, h_x = h

            distance = abs(c_y - h_y) + abs(c_x - h_x)
            min_house[idx_h] = min(min_house[idx_h], distance)

    min_distance = min(min_distance, sum(min_house))

print(min_distance)
