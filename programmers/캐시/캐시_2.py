from collections import deque


def solution(cache_size, cities):
    cities = list(map(lambda x: x.lower(), cities))
    # maxlen 값을 설정하면
    # deque 가 다 찼는데 새로운 요소를 append 할 경우
    # 맨 처음에 들어온 요소가 자동으로 제거된다
    cache = deque(maxlen=cache_size)

    total_time = 0

    for city in cities:
        if city in cache:
            total_time += 1
            cache.remove(city)
            cache.append(city)
        else:
            total_time += 5
            cache.append(city)

    return total_time


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
