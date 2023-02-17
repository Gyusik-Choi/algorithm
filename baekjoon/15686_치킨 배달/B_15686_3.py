def get_chicken_store_combinations(num, num_limit, cnt, cnt_limit, combination):
    if cnt == cnt_limit:
        chicken_store_combinations.append(combination[:])
        return

    for n in range(num, num_limit):
        combination.append(n)
        get_chicken_store_combinations(n + 1, num_limit, cnt + 1, cnt_limit, combination)
        combination.pop()


N, M = map(int, input().split())
city_info = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken_store = []

for i, city in enumerate(city_info):
    for j, c in enumerate(city):
        if c == 1:
            house.append([i, j])
        elif c == 2:
            chicken_store.append([i, j])

# 최대 M 개의 치킨집 조합
chicken_store_combinations = []

get_chicken_store_combinations(0, len(chicken_store), 0, M, [])

# 어느 집이 어떤 치킨집 선택 하는건 어떻게 해야 할지?
# => 집 마다 치킨집 조합의 치킨집 마다 거리를 계산 하여 최소 거리의 치킨집 선택

# 3중 for 문
# 치킨집 조합
# 집
# 조합내 각 치킨 집

min_total = float('inf')

for i, chicken in enumerate(chicken_store_combinations):
    temp_min_total = 0

    for k, h in enumerate(house):
        h_y, h_x = h

        min_distance_per_house = float('inf')

        for j, c in enumerate(chicken):
            c_y, c_x = chicken_store[c]

            min_distance_per_house = min(min_distance_per_house, abs(h_y - c_y) + abs(h_x - c_x))

        temp_min_total += min_distance_per_house

        if temp_min_total > min_total:
            break

    min_total = min(min_total, temp_min_total)

print(min_total)
