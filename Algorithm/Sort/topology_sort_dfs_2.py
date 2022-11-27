def dfs(start, visited, stack) -> list:
    global is_cycle

    # 여기서 stack 에 start 를 집어 넣으면
    # cycle 판별을 제대로 하지 못한다
    # 아래 else 문의 if end not in stack:
    # 조건을 제대로 동작하게 하려면
    # 아직 start 가 stack 에 들어가지 않아야 한다
    # stack.append(start)

    for end in edges[start]:
        if not visited[end]:
            visited[end] = True
            dfs(end, visited, stack)
        else:
            if end not in stack:
                is_cycle = True
                return []

    # for 문을 완료한 후 stack 에 start 를 넣는다
    stack.append(start)

    return stack


def topology_sort():
    answer = []
    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i] and not is_cycle:
            # 위의 dfs 함수에서는 end 에 대해서 방문처리를 하는데
            # start 에 대해선 하지 않고 있어서
            # 여기서 start 에 대한 방문 처리를 미리 수행하고
            # dfs 함수를 호출한다
            visited[i] = True
            answer += dfs(i, visited, [])

    return list(reversed(answer))


n = 7
m = 7
edge_info = [
    '1 2',
    '1 5',
    '2 3',
    '3 4',
    '4 6',
    '5 6',
    '6 3',
]

edges = {i: [] for i in range(n + 1)}

for idx, edge in enumerate(edge_info):
    s, e = map(int, edge.split(' '))
    edges[s].append(e)

is_cycle = False
arr = topology_sort()

if not is_cycle:
    while arr:
        print(arr.pop(), end=" ")
    print()
else:
    print('cycle')

# 참고
# https://reakwon.tistory.com/140
# https://sorjfkrh5078.tistory.com/36
# https://itholic.github.io/python-reverse-reversed/
