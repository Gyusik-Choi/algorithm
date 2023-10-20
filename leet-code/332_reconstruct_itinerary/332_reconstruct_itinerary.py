from collections import defaultdict, deque


def find_itinerary(tickets: list[list[str]]) -> list[str]:
    graph = defaultdict(deque)

    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []

    def dfs(v):
        while graph[v]:
            dfs(graph[v].popleft())
        route.append(v)

    dfs('JFK')
    return route[::-1]


print(find_itinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))
print(find_itinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"], ["JFK", "ORT"], ["ORT", "JFK"]]))
print(find_itinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))

# "틀린풀이"의 경우
# lexical order 로 탐색은 수행 하지만
# 모든 여행 경로를 연결해서 탐색하지 못할 수 있고
# 그리고 모든 티켓을 사용하지 못할 수 있다
# find_itinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]])
# 이 경우가 예시다
# ['JFK', 'NRT', 'JFK', 'KUL'] 이 나와야 하는데
# ['JFK', 'KUL', 'NRT', 'JFK'] 가 나온다
# JFK 에서 KUL 이 단어 순서상 먼저지만
# NRT 보다 KUL 을 먼저 방문하면 더 이상 탐색을 이어갈 수 없다
# KUL 에서는 JFK 로 돌아갈 수 없고 탐색이 종료된다
# 하지만 아직 사용하지 않은 티켓이 남아서 탐색이 종료되면 안 된다
# KUL 을 먼저 가면 안되고 NRT 를 가야
# JFK -> NRT 를 갔다가 다시 NRT -> JFK 로 돌아올 수 있고
# 그리고 JFK -> KUL 을 갈 수 있다
