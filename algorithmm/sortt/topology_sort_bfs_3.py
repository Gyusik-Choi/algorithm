# 백준 3665 문제를 구글링 하면서
# 바로 인접한 정점 외에 하위의 정점도 모두 저장하는 방식을 사용하는 것을 보고
# 이것이 가능한지 직접 해보고 싶어서 작성해 보았다
# 나동빈 님의 블로그 글의 그래프를 참고하여 인접 정점 뿐만 아니라 하위의 정점들도
# 모두 입력으로 넣어서 수행했고 결과적으로 같은 값을 얻을 수 있었다
# 정점들을 넣을 때 진입 차수를 함께 올려주어서 해당 정점에서 방문할 수 있는 정점들을 보더라도
# 진입 차수가 0이 아니면 큐에 넣을 수 없기 때문이다

# 7 18
# 1 2
# 1 3
# 1 4
# 1 5
# 1 6
# 1 7
# 2 3
# 2 4
# 2 6
# 2 7
# 3 4
# 3 6
# 3 7
# 4 6
# 4 7
# 5 6
# 5 7
# 6 7

def bfs(q, levels):
    answer = []
    while q:
        node = q.pop(0)
        answer.append(node)

        for i in range(len(adj[node])):
            levels[adj[node][i]] -= 1
            if not levels[adj[node][i]]:
                q.append(adj[node][i])

    return answer


def topology_sort(node_level):
    queue = []
    for i in range(1, N + 1):
        if not node_level[i]:
            queue.append(i)

    return bfs(queue, node_level)


N, M = map(int, input().split())
adj = {i: [] for i in range(1, N + 1)}
level = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    adj[A].append(B)
    level[B] += 1

print(topology_sort(level))

# 참고
# https://www.acmicpc.net/problem/3665
# https://m.blog.naver.com/ndb796/221236874984
# https://mapocodingpark.blogspot.com/2020/03/BOJ3665.html
