from collections import defaultdict
import heapq


def find_cheapest_price(n: int, flights: list[list[int]], src: int, dst: int, k: int):
    node = defaultdict(list)

    for f, t, p in flights:
        node[f].append([t, p])

    # 비용, 횟수, 출발점
    heap = [[0, 0, src]]
    price = [float('inf')] * n
    price[src] = 0
    cnt = [0] * n

    while heap:
        start_price, start_cnt, start = heapq.heappop(heap)

        if start == dst:
            return start_price

        if start_cnt > k:
            continue

        for end, end_price in node[start]:
            # 가격이 저렴 하거나 횟수가 작은 경우
            if price[end] > start_price + end_price or cnt[end] > start_cnt:
                price[end] = start_price + end_price
                cnt[end] = start_cnt
                heapq.heappush(heap, [price[end], start_cnt + 1, end])

    if price[dst] == float('inf'):
        return -1
    return price[dst]


print(find_cheapest_price(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1))
# 700
print(find_cheapest_price(5, [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]], 0, 2, 2))
# 7

# 참고
# https://github.com/onlybooks/python-algorithm-interview/issues/104
