# 입력
# 4 6
# 1 2 3
# 1 3 2
# 1 4 5
# 2 3 3
# 3 4 -4
# 4 2 -4

# 플로이드 와샬이 모든 정점들의 최소 거리를 구한다면
# 벨만 포드는 다익스트라와 유사하게 한 정점에서 나머지 정점들로 가는 최소 거리를 구하는 공통점이 있다
# 다만 다익스트라와의 차이는 벨만 포드는 음의 순환을 체크할 수 있다
# 이 코드에서는 1번 정점을 기준으로 나머지 정점들과의 최소 거리를 구한다
# 백준 11657 문제가 이와 거의 같은 방식으로 풀이할 수 있다(마지막 출력 부분만 수정하면 됨)

def bellman_ford():
    # V - 1번 edge relaxation 반복(edge relaxation -> 가중치를 감소, 경감)
    # 그리고 1번의 추가적인 edge relaxation 을 통해서 음의 순환 검사
    # 총 V번 검사 (V - 1회 + 1회)
    for i in range(V):
        # 매번 반복마다 모든 간선을 확인한다(다익스트라와의 차이)
        for j in range(E):
            start = edges[j][0]
            end = edges[j][1]
            value = edges[j][2]
            if bf[start - 1] != INF and bf[end - 1] > bf[start - 1] + value:
                bf[end - 1] = bf[start - 1] + value
                # 가중치가 감소했는데 V 번째 검사라면 음의 순환이 존재한다는 것
                if i == V - 1:
                    return False
    return True


V, E = map(int, input().split())
edges = []
for _ in range(E):
    s, e, v = map(int, input().split())
    edges.append([s, e, v])

INF = float('inf')
bf = [INF] * V
bf[0] = 0

val = bellman_ford()
if not val:
    print(-1)
else:
    print(bf)

# 참고
# https://yabmoons.tistory.com/365
# https://ratsgo.github.io/data%20structure&algorithm/2017/11/27/bellmanford/
# https://ssungkang.tistory.com/entry/Algorithm-%EB%B2%A8%EB%A7%8C%ED%8F%AC%EB%93%9CBellman-Ford-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
# https://m.blog.naver.com/kks227/220796963742
