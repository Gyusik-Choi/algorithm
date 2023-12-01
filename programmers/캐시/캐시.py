from collections import deque


def solution(cache_size, cities):
    cities = list(map(lambda x: x.lower(), cities))
    cache = deque()

    total_time = 0

    for city in cities:
        if city in cache:
            total_time += 1
            cache.remove(city)
            cache.append(city)
        else:
            total_time += 5
            if cache and len(cache) >= cache_size:
                cache.popleft()
            # 아래의 if 문이 없으면
            # cache_size 가 0인데도
            # 계속 cache 에 넣게 된다
            # 그러면 위의 if 문인
            # if city in cache 조건을 만족해서
            # cache miss 인데
            # cache hit 가 돼서 오답이 나올 수 있다
            if cache_size:
                cache.append(city)

    return total_time


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
