from collections import defaultdict
from functools import reduce


def solution(clothes):
    item = defaultdict(int)

    for name, kind in clothes:
        item[kind] += 1

    return reduce(lambda acc, cur: acc * cur, list(map(lambda x: item[x] + 1, item.keys()))) - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
print(solution([["yellow_hat", "headgear"],  ["green_turban", "headgear"], ["blue_sunglasses", "eyewear"],
                ["crow_mask", "face"]]))
