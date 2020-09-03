from collections import deque


def solution(cachesize, cities):
    answer = 0
    # 데크는 최대 크기를 지정할 수 있다.
    # 최대 크기 지정하여 최대 크기를 넘어가면 앞의 요소가 지워진다.
    # 이 문제를 풀이하는데 있어서 캐시 크기를 넘어섰는지 고려하지 않아도 되므로 풀이하기 편해진다.
    cache = deque(maxlen=cachesize)
    # 캐시 사이즈가 0일 경우를 따로 예외처리 안하더라도 데크의 maxlen 에 의해 답을 구하는데는
    # 문제가 없지만 좀 더 빠르게 구하기 위해 추가.
    if cachesize == 0:
        answer += len(cities) * 5
        return answer
    for i in cities:
        # 대소문자 구분하지 않는다는 조건이 있으므로 모두 소문자 처리.
        i = i.lower()
        # 캐시 안에 있을 경우
        if i in cache:
            cache.remove(i)
            cache.append(i)
            answer += 1
        # 캐시 안에 없을 경우
        else:
            cache.append(i)
            answer += 5
    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul"]))
