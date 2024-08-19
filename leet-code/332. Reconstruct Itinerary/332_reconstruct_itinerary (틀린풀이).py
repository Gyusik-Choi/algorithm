def get_edges(tickets):
    edges = dict()

    for [start, end] in tickets:
        if start not in edges:
            edges[start] = [end]
        else:
            edges[start].append(end)

    # 오름차순 정렬
    for v in edges.values():
        v.sort()

    return edges


def get_visited(edges):
    visited = dict()

    for k, v in edges.items():
        visited[k] = [False] * len(v)

    return visited


def find_itinerary(tickets):
    # 중복 방문이 가능
    # 이 부분 처리를 어떻게 할지
    # dict 2개
    # 하나는 방문 가능한 곳
    # 다른 하나는 방문 여부

    # 방문 가능한 곳
    edges = get_edges(tickets)

    # 방문 여부
    visited = get_visited(edges)

    def search(start, answer):
        answer.append(start)

        if start in edges:
            for idx, vertex in enumerate(edges[start]):
                if visited[start][idx]:
                    continue

                visited[start][idx] = True
                search(vertex, answer)

        return answer

    return search("JFK", [])


print(find_itinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
print(find_itinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(find_itinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))
# ["JFK", "NRT", "JFK", "KUL"]
