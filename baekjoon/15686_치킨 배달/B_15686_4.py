def get_chicken_store_combinations(temp, cnt, cnt_limit, num, num_limit):
    if cnt == cnt_limit:
        chicken_store_combinations.append(temp[:])
        return

    for n in range(num, num_limit):
        temp.append(n)
        get_chicken_store_combinations(temp, cnt + 1, cnt_limit, n + 1, num_limit)
        temp.pop()


N, M = map(int, input().split())
chicken_store = []
house = []

for i in range(N):
    row = list(map(int, input().split()))

    for j, r in enumerate(row):
        if r == 1:
            house.append([i, j])
            continue

        if r == 2:
            chicken_store.append([i, j])

chicken_store_combinations = []
get_chicken_store_combinations([], 0, M, 0, len(chicken_store))

min_distance = float('inf')

for i, store_combination in enumerate(chicken_store_combinations):
    temp_min_distance = 0

    for k, h in enumerate(house):
        temp_dist = float('inf')
        house_y, house_x = h

        for j, store in enumerate(store_combination):
            store_y, store_x = chicken_store[store]
            temp_dist = min(temp_dist, abs(house_y - store_y) + abs(house_x - store_x))

        temp_min_distance += temp_dist

    min_distance = min(min_distance, temp_min_distance)

print(min_distance)
